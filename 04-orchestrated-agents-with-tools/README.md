# 🛠️ Orchestrated Agents with Tools - External API Integration

Welcome to the advanced world of tool-enhanced agent orchestration! This folder contains comprehensive tutorials that show you how to integrate external APIs, services, and cloud workflows with Azure AI agents to create powerful, real-world applications.

## 📚 What's In This Folder

### 💱 [04.1 - OpenAPI Currency Exchange Tutorial](04.1-openapi_currency_exchange_tutorial.ipynb)
**Master external API integration using OpenAPI specifications**

Learn how to connect your agents to real-world services:
- 🎯 Understanding OpenAPI tools for external API integration
- 🌐 Connecting to Frankfurter currency exchange API
- 🔧 Azure AI Foundry SDK approach with OpenApiTool
- 🚀 Semantic Kernel approach with AzureAIAgent wrappers
- 💱 Real-time currency conversion and exchange rate queries
- 🔄 Comparative analysis of both integration approaches

**Perfect for**: Developers who want to connect their agents to external APIs and services for real-time data access and functionality.

### 🏦 [04.2 - Hybrid OpenAPI + Semantic Kernel Plugins Tutorial](04.2-hybrid_openapi_and_plugins_tutorial.ipynb)
**Combine external APIs with local plugins for comprehensive solutions**

Explore the power of hybrid architectures:
- 🔗 Combining OpenAPI tools with Semantic Kernel plugins
- 🏦 Banking scenario with local account data and external currency rates
- 📊 Local data processing with custom business logic
- 🌍 External API integration for real-time information
- 💰 Complex financial workflows requiring both approaches
- 🎯 Best practices for hybrid agent architectures

**Perfect for**: Developers building enterprise solutions that need both internal business logic and external service integration.

### 🔄 [04.3 - Logic Apps + Hybrid Tutorial](04.3-logic_apps_hybrid_tutorial.ipynb)
**Integrate Azure Logic Apps workflows with AI agent intelligence**

Master cloud workflow automation with AI coordination:
- ⚡ Azure Logic Apps integration for automated workflows
- 📧 Email notifications and business process automation
- 🔌 Semantic Kernel plugins for local data processing
- 🎭 Hybrid orchestration combining cloud automation with AI
- 📊 Business intelligence workflows with automated triggers
- 🔄 End-to-end scenarios from data analysis to notification

**Perfect for**: Developers who want to build intelligent automation systems that combine AI decision-making with enterprise workflow automation.

## 🎯 Learning Path

We recommend following the tutorials in this order:

1. **Start with 04.1** - Master external API integration fundamentals
2. **Progress to 04.2** - Learn hybrid architectures combining multiple tool types
3. **Complete with 04.3** - Integrate cloud workflows with AI orchestration

**Prerequisites**: Complete the [01-agent-basics](../01-agent-basics/), [02-agent-custom-functions](../02-agent-custom-functions/), and [03-orchestrated-agents](../03-orchestrated-agents/) tutorials first.

## 📋 Prerequisites

Before starting these tutorials, ensure you have:

### Previous Knowledge
- ✅ Completed all previous tutorial folders (01, 02, 03)
- ✅ Understanding of Azure AI Agents and custom functions
- ✅ Knowledge of agent orchestration patterns
- ✅ Familiarity with REST APIs and JSON

### Azure Resources
- ✅ Azure subscription with sufficient permissions
- ✅ Azure AI Foundry project
- ✅ Deployed AI model (GPT-4, GPT-3.5-turbo, etc.)
- ✅ Azure OpenAI resource (for Semantic Kernel scenarios)
- ✅ Azure Logic Apps (for workflow automation scenarios)

### Environment Setup
- ✅ Python 3.8+ installed
- ✅ Jupyter Notebook or VS Code with notebook support
- ✅ Azure CLI (recommended for authentication)
- ✅ Network access to external APIs (Frankfurter, etc.)

### Environment Variables
Configure your Azure AI services by filling in the `.env` file at the project root level:

```bash
# Navigate to the project root and edit the .env file
cd ../../  # Go to azure-ai-agents-playbook root
# Edit .env file with your Azure AI configuration
```

The `.env` file should contain your Azure AI project details:
```properties
# Required for all tutorials
PROJECT_ENDPOINT="https://your-project.services.ai.azure.com/api/projects/your-project"
MODEL_DEPLOYMENT_NAME="your-model-deployment-name"

# Required for Semantic Kernel scenarios (04.1, 04.2)
AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com/"
AZURE_OPENAI_API_KEY="your-openai-api-key"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your-chat-deployment"

# Required for Logic Apps integration (04.3)
AZURE_SUBSCRIPTION_ID="your-subscription-id"
AZURE_RESOURCE_GROUP_NAME="your-resource-group-name"

# Optional: For advanced scenarios
REASONING_MODEL_DEPLOYMENT_NAME="your-reasoning-model"
```

💡 **Tip**: The `.env` file is already present in the project root with example values. Simply update it with your Azure AI project details.

### Required Packages
Each tutorial will install its required packages, but you can install them all upfront:

```bash
pip install azure-ai-agents azure-identity semantic-kernel azure-mgmt-logic requests
```

## 🔑 Key Concepts Covered

### 🛠️ **External Tool Integration**

**What tool integration enables:**
- 🌐 **Real-time Data Access**: Live currency rates, weather, stock prices
- 🔗 **Service Integration**: Payment processing, communication, automation
- 📊 **Data Enrichment**: Combine internal data with external insights
- ⚡ **Workflow Automation**: Trigger business processes and notifications
- 🎯 **Dynamic Capabilities**: Extend agent functionality without code changes

### 🔧 **Tool Integration Approaches**

#### OpenAPI Tool Integration
- **Method**: `OpenApiTool` with standardized API specifications
- **Benefits**: Standardized integration, automatic parameter handling, documentation-driven
- **Use Cases**: Currency exchange, weather APIs, public data services
- **Example**: Frankfurter currency exchange API integration

#### Hybrid Plugin + API Architecture
- **Method**: Combine Semantic Kernel plugins with external APIs
- **Benefits**: Local + external data, secure business logic, flexible architectures
- **Use Cases**: Banking systems, enterprise applications, multi-source intelligence
- **Example**: Local banking data + external currency rates

#### Workflow Automation Integration
- **Method**: Azure Logic Apps integration with AI decision-making
- **Benefits**: Enterprise workflow automation, scalable process orchestration
- **Use Cases**: Business process automation, notification systems, approval workflows
- **Example**: Data analysis triggering automated email notifications

### 🏗️ **Advanced Architecture Patterns**

- **API Gateway Patterns**: Centralized external service management
- **Hybrid Data Processing**: Local business logic + external data sources
- **Workflow Orchestration**: AI-driven business process automation
- **Error Resilience**: Graceful handling of external service failures
- **Security Integration**: Secure API authentication and data handling

## 🚀 Quick Start Guide

### Option 1: OpenAPI Currency Exchange (External API)
```python
from azure.ai.agents import AgentsClient
from azure.ai.agents.models import OpenApiTool, OpenApiAnonymousAuthDetails

# Load OpenAPI specification
with open("currency_exchange.json", "r") as f:
    currency_openapi_spec = json.loads(f.read())

# Create OpenAPI tool
auth = OpenApiAnonymousAuthDetails()
currency_tool = OpenApiTool(
    name="currency_exchange",
    spec=currency_openapi_spec,
    description="Get current exchange rates from Frankfurter API",
    auth=auth
)

# Create agent with external API access
agent = client.create_agent(
    model=os.environ["MODEL_DEPLOYMENT_NAME"],
    name="currency_expert",
    instructions="You help with currency conversion using live exchange rates.",
    tools=currency_tool.definitions
)

# Agent automatically calls external API when needed
```

### Option 2: Hybrid Plugin + API Architecture (Best of Both)
```python
from semantic_kernel.agents import AzureAIAgent
from semantic_kernel.functions import kernel_function

# Local business logic plugin
class BankingPlugin:
    @kernel_function(description="Get account balances")
    def get_account_balances(self) -> str:
        # Access internal banking data securely
        return json.dumps(account_data)

# Create hybrid agent with both local and external capabilities
async with DefaultAzureCredential() as creds:
    client = AzureAIAgent.create_client(
        credential=creds, 
        endpoint=os.environ["PROJECT_ENDPOINT"]
    )
    
    # Agent with OpenAPI tool + local plugin
    agent = AzureAIAgent(
        client=client,
        definition=await client.agents.create_agent(
            model=os.environ["MODEL_DEPLOYMENT_NAME"],
            name="banking_assistant",
            instructions="Provide banking services with live exchange rates.",
            tools=currency_tool.definitions  # External API
        ),
        plugins=[BankingPlugin()]  # Local business logic
    )
```

### Option 3: Logic Apps Workflow Integration (Cloud Automation)
```python
from azure.mgmt.logic import LogicManagementClient

# Integration with Azure Logic Apps
class AzureLogicAppTool:
    def register_logic_app(self, logic_app_name: str, trigger_name: str):
        # Register workflow callback URL
        callback = self.logic_client.workflow_triggers.list_callback_url(
            resource_group_name=self.resource_group,
            workflow_name=logic_app_name,
            trigger_name=trigger_name
        )
        self.callback_urls[logic_app_name] = callback.value

    def invoke_logic_app(self, logic_app_name: str, payload: Dict[str, Any]):
        # Trigger business workflow
        response = requests.post(url=self.callback_urls[logic_app_name], json=payload)

# Create agent that can trigger automated workflows
agent = client.create_agent(
    model=os.environ["MODEL_DEPLOYMENT_NAME"],
    name="automation_assistant",
    instructions="Analyze data and trigger appropriate business workflows.",
    tools=[logic_app_function]
)
```

## 🏗️ What You'll Build

By the end of these tutorials, you'll have built:

### 🌐 **External API Integration Systems**
1. **Currency Exchange Agent** - Real-time currency conversion using external APIs
2. **Multi-API Coordination** - Agents that combine multiple external services
3. **Error-Resilient Integration** - Graceful handling of external service failures
4. **Authentication Patterns** - Secure API access and credential management

### 🏦 **Hybrid Business Applications**
1. **Banking Assistant** - Local account data + external exchange rates
2. **Financial Intelligence** - Multi-source data analysis and insights
3. **Investment Advisor** - Portfolio data + market APIs + news feeds
4. **Business Intelligence** - Internal metrics + external market data

### 🔄 **Workflow Automation Systems**
1. **Data Analysis Pipelines** - Automated processing and notification workflows
2. **Business Process Automation** - AI-driven decision making with workflow triggers
3. **Alert and Notification Systems** - Intelligent monitoring with automated responses
4. **Approval Workflows** - AI-assisted business process management

## 🔍 Troubleshooting

### Common Issues

**OpenAPI Tool Configuration Errors**
```
Problem: OpenAPI tools not working correctly
Solutions:
- Verify OpenAPI specification format and validity
- Check API endpoint accessibility and authentication
- Ensure proper OpenApiAnonymousAuthDetails or auth configuration
- Test API endpoints manually before agent integration
```

**External API Authentication Failures**
```
Problem: API calls failing due to authentication
Solutions:
- Verify API keys and credentials are correct
- Check authentication method matches API requirements
- Implement proper error handling for auth failures
- Monitor API rate limits and quotas
```

**Hybrid Architecture Complexity**
```
Problem: Complex interactions between local and external tools
Solutions:
- Test local plugins independently first
- Verify external API integration separately
- Use clear agent instructions for tool selection
- Implement proper error handling for both tool types
```

**Logic Apps Integration Issues**
```
Problem: Workflow triggers not working
Solutions:
- Verify Logic App permissions and callback URLs
- Check Azure subscription and resource group access
- Test Logic App triggers manually in Azure portal
- Implement fallback mechanisms for workflow failures
```

**Network and Connectivity Problems**
```bash
# Test external API connectivity
curl -X GET "https://api.frankfurter.dev/v1/latest?base=USD"

# Verify Azure authentication
az account show
az login --use-device-code

# Check Logic Apps access
az logicapp list --resource-group your-resource-group
```

## 📖 Additional Resources

- [Azure AI Agents OpenAPI Tools Documentation](https://docs.microsoft.com/azure/ai-services/agents/tools/openapi/)
- [Semantic Kernel External API Integration](https://learn.microsoft.com/semantic-kernel/plugins/external-apis/)
- [Azure Logic Apps Integration Guide](https://docs.microsoft.com/azure/logic-apps/)
- [OpenAPI Specification Documentation](https://swagger.io/specification/)
- [REST API Security Best Practices](https://docs.microsoft.com/azure/architecture/best-practices/api-security/)

## 🎯 Next Steps

After mastering orchestrated agents with external tools, explore:

- **[05-orchestrated-agents-with-custom-openapi-tools](../05-orchestrated-agents-with-custom-openapi-tools/)** - Building custom API integrations and advanced tool patterns
- **[06-magentic-one-orchestration](../06-magentic-one-orchestration/)** - Advanced multi-agent orchestration with sophisticated tool coordination
- **[07-voice-orchestration](../07-voice-orchestration/)** - Voice-enabled agent interactions and tool usage

## 💡 Tips for Success

1. **Start with Simple APIs** - Test basic external API integration before complex scenarios
2. **Secure Your Integrations** - Always use proper authentication and validate inputs
3. **Handle Failures Gracefully** - External services can fail; implement robust error handling
4. **Monitor API Usage** - Track external API consumption and costs
5. **Test Incrementally** - Verify each tool individually before combining them
6. **Document Dependencies** - Keep track of external service requirements and limitations
7. **Design for Resilience** - Build systems that work even when external services are unavailable

## 🌟 Tool Integration Best Practices

### ✅ **API Integration Design**
- **Clear Documentation**: Thoroughly document all external API dependencies
- **Error Handling**: Implement comprehensive error handling for external service failures
- **Rate Limiting**: Respect API rate limits and implement appropriate throttling
- **Authentication Security**: Securely manage API keys and authentication tokens
- **Response Validation**: Validate external API responses before processing

### ✅ **Hybrid Architecture Patterns**
- **Separation of Concerns**: Keep local business logic separate from external data access
- **Fallback Mechanisms**: Provide fallbacks when external services are unavailable
- **Data Validation**: Validate all external data before combining with internal data
- **Performance Optimization**: Cache external API responses when appropriate
- **Security Boundaries**: Maintain security boundaries between internal and external data

### ✅ **Workflow Integration**
- **Process Documentation**: Document all automated workflow triggers and processes
- **Monitoring and Alerting**: Monitor workflow execution and success rates
- **Rollback Strategies**: Implement rollback mechanisms for failed workflows
- **Testing Strategies**: Test workflow automation in staging environments
- **Compliance**: Ensure workflow automation meets regulatory requirements

### ✅ **Production Considerations**
- **Scalability**: Design for horizontal scaling with multiple external dependencies
- **Monitoring**: Implement comprehensive monitoring for all external integrations
- **Security**: Regular security audits of all external API integrations
- **Cost Management**: Monitor and optimize costs for external service usage
- **Disaster Recovery**: Plan for scenarios where external services become unavailable

---

🎉 **Ready to build sophisticated agent systems with external tool integration?** Start with basic OpenAPI integration and progress to complex hybrid architectures that combine the best of local intelligence and external services!
