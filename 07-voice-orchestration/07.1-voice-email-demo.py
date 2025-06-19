# Voice-Activated Email Agent Demo
# Voice-controlled agent that can send emails via Logic Apps

# Import necessary libraries and load environment variables
import os
import asyncio
import json
import requests
from datetime import datetime
from typing import Annotated, Dict, Any, Callable, Set
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(override=True)

# Import Azure AI Foundry SDK
from azure.ai.agents import AgentsClient
from azure.ai.agents.models import ToolSet, FunctionTool
from azure.identity import DefaultAzureCredential
from azure.mgmt.logic import LogicManagementClient

# Import our voice module
from voice import AgentVoice

print("📦 All packages imported successfully!")
print("🔧 Ready to create voice-enabled email agent!")

# Verify environment variables
required_vars = ['PROJECT_ENDPOINT', 'MODEL_DEPLOYMENT_NAME']
optional_vars = ['AZURE_SUBSCRIPTION_ID', 'AZURE_RESOURCE_GROUP_NAME']

for var in required_vars:
    if var in os.environ:
        print(f"✅ {var} is set")
    else:
        print(f"❌ {var} is missing!")

for var in optional_vars:
    if var in os.environ:
        print(f"✅ {var} is set (for Logic Apps)")
    else:
        print(f"⚠️ {var} is missing (Logic Apps features disabled)")

# Azure Logic Apps Tool for Email Functionality
class EmailLogicAppTool:
    """Tool for sending emails via Azure Logic Apps"""

    def __init__(self, subscription_id: str = None, resource_group: str = None, credential=None):
        self.subscription_id = subscription_id
        self.resource_group = resource_group
        self.callback_urls = {}
        
        if subscription_id and resource_group:
            try:
                credential = credential or DefaultAzureCredential()
                self.logic_client = LogicManagementClient(credential, subscription_id)
                print("✅ Logic Apps client initialized")
            except Exception as e:
                print(f"⚠️ Logic Apps initialization failed: {e}")
                self.logic_client = None
        else:
            self.logic_client = None
            print("⚠️ Logic Apps not configured (missing subscription/resource group)")

    def register_logic_app(self, logic_app_name: str, trigger_name: str = "When_a_HTTP_request_is_received") -> bool:
        """Register a Logic App for email sending"""
        if not self.logic_client:
            print("⚠️ Logic Apps client not available")
            return False
            
        try:
            callback = self.logic_client.workflow_triggers.list_callback_url(
                resource_group_name=self.resource_group,
                workflow_name=logic_app_name,
                trigger_name=trigger_name,
            )
            
            if callback.value:
                self.callback_urls[logic_app_name] = callback.value
                print(f"✅ Registered email Logic App: {logic_app_name}")
                return True
            else:
                print(f"⚠️ No callback URL found for Logic App: {logic_app_name}")
                return False
        except Exception as e:
            print(f"⚠️ Failed to register Logic App {logic_app_name}: {e}")
            print("💡 This is expected if the Logic App doesn't exist - emails will be simulated")
        
        return False

    def invoke_logic_app(self, recipient: str, subject: str, body: str, logic_app_name: str = "agent-logic-apps") -> Dict[str, Any]:
        """Send email via Logic Apps or simulate if not configured"""
        
        if logic_app_name in self.callback_urls:
            # Send via actual Logic App
            try:
                payload = {
                    "to": recipient,
                    "subject": subject,
                    "body": body,
                    "timestamp": datetime.now().isoformat()
                }
                
                response = requests.post(url=self.callback_urls[logic_app_name], json=payload, timeout=30)
                
                if response.ok:
                    return {"status": "success", "message": f"Email sent to {recipient} via Logic Apps"}
                else:
                    return {"status": "error", "message": f"Logic App failed: {response.status_code}"}
                    
            except Exception as e:
                return {"status": "error", "message": f"Email sending failed: {str(e)}"}
        else:
            # Simulate email sending
            print(f"📧 SIMULATED EMAIL:")
            print(f"   To: {recipient}")
            print(f"   Subject: {subject}")
            print(f"   Body: {body}")
            print(f"   Timestamp: {datetime.now()}")
            return {"status": "simulated", "message": f"Email simulated (sent to {recipient})"}


def create_send_email_function(service: EmailLogicAppTool, logic_app_name: str) -> Callable[[str, str, str], str]:
    """
    Returns a function that sends an email by invoking the specified Logic App.
    """
    def send_email_via_logic_app(to: str, subject: str, body: str) -> str:
        """
        Sends an email by invoking the specified Logic App with the given recipient, subject, and body.
        """
        result = service.invoke_logic_app(to, subject, body, logic_app_name)
        return json.dumps(result)

    return send_email_via_logic_app



print("✅ Email tool ready!")

# Step 2: Create a voice-controlled email agent
async def create_email_agent():
    """Create an Azure AI agent with email capabilities."""

    # Get required environment variables
    model_deployment_name = os.environ.get("MODEL_DEPLOYMENT_NAME")
    endpoint = os.environ.get("PROJECT_ENDPOINT")
    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
    resource_group = os.environ.get("AZURE_RESOURCE_GROUP_NAME")

    if not model_deployment_name or not endpoint:
        raise ValueError("Missing required environment variables: MODEL_DEPLOYMENT_NAME and PROJECT_ENDPOINT")

    # Create the email tool instance
    credential = DefaultAzureCredential()
    agents_client = AgentsClient(endpoint=endpoint, credential=credential)

    # Initialize email tool
    # Configure Azure Logic Apps Tool
    logic_app_tool = EmailLogicAppTool(
        subscription_id=subscription_id,
        resource_group=resource_group,
    )

    # Register a Logic App workflow (replace with your actual Logic App details)
    logic_app_name = "agent-logic-apps"  # Your Logic App name
    trigger_name = "When_a_HTTP_request_is_received"  # Your trigger name (often "manual" or "request")

    # Register the Logic App with the tool
    logic_app_tool.register_logic_app(
        logic_app_name=logic_app_name,
        trigger_name=trigger_name
    )    # Create the email function for this specific Logic App
    send_email_function = create_send_email_function(logic_app_tool, logic_app_name)

    print(f"✅ Logic App tool configured for: {logic_app_name}")
    print(f"🔧 Trigger: {trigger_name}")
    print(f"📧 Email function created for workflow integration")

    # Prepare the function tools for the agent
    functions_to_use: Set = {
        send_email_function,  # This references the AzureLogicAppTool instance via closure
    }

    # Create agent with proper toolset
    with agents_client:
        # Create function tool and toolset
        functions = FunctionTool(functions=functions_to_use)
        toolset = ToolSet()
        toolset.add(functions)

        # Enable auto function calls - this is key for actual execution
        agents_client.enable_auto_function_calls(toolset)

        agent = agents_client.create_agent(
            model=model_deployment_name,
            name="voice-email-assistant",
            instructions="""You are a helpful voice-controlled email assistant. 

CAPABILITIES:
📧 EMAIL: Send emails to people with subject and body content

VOICE INTERACTION GUIDELINES:
- Speak naturally and conversationally since this is a voice interface
- Be encouraging and helpful
- Confirm email details before sending them
- Ask for clarification if recipient, subject, or content is unclear
- Always confirm the email was sent successfully

EXAMPLES:
- "Send an email to john@company.com about the meeting" → Use send_email_via_logic_app function
- "Email sarah@company.com with subject Project Update and tell her the project is complete"
- "Send a message to admin@company.com saying the quarterly report is ready"

When sending emails:
- Confirm the recipient email address
- Provide a clear subject line
- Create appropriate professional content if not specified
- Always explain what email you're sending and to whom.

The available emails for you to use are:
- Samer with email: ehsamer@hotmail.com
- Samer with email: samer.elhousseini@microsoft.com

""",
            toolset=toolset
    )  
          
    print(f"🤖 Created email agent: {agent.name}")
    print(f"🔧 Agent has email sending capabilities")
    print(f"🆔 Agent ID: {agent.id}")
    
    return agent, agents_client

async def main():
    """Main function to run the voice-activated email assistant demo."""
    
    print("🎙️ Starting Voice-Activated Email Assistant Demo")
    print("=" * 60)
    
    try:
        # Create the email agent
        print("Creating email agent with Logic Apps integration...")
        agent, agents_client = await create_email_agent()
        
        # Create voice interface with the agent  
        print("\n🎤 Setting up voice interface...")
        av = AgentVoice(agent_id=agent.id)
        
        print("\n🗣️ Voice interface ready!")
        print("Sample voice commands you can try:")
        print("• 'Send an email to john@company.com about the quarterly results'")
        print("• 'Email sarah@company.com with subject Meeting Update'")
        print("• 'Send a message to admin@company.com saying the project is complete'")
        print("• 'Email the team about tomorrow's presentation'")
        print("• 'Send an urgent email to manager@company.com'")
        print("\nPress 'q' and Enter anytime to quit.")
        print("=" * 60)
        
        # The voice module will handle communication with the agent directly
        # No need for manual tool handling since we're using auto function calls
        
        # Start the voice conversation
        await av.connect()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        print("\n👋 Demo completed!")

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("🎙️ VOICE-CONTROLLED EMAIL ASSISTANT")
    print("Features: Send emails via Logic Apps with voice commands")
    print("=" * 60)
    
    # Run the main demo
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 Demo interrupted by user")
    except Exception as e:
        print(f"❌ Demo failed: {e}")
        import traceback
        traceback.print_exc()
