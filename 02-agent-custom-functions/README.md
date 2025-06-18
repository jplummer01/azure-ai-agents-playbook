# 🔧 Agent Custom Functions - Extending Agent Capabilities

Welcome to the next level of Azure AI Agents development! This folder contains comprehensive tutorials that show you how to supercharge your agents by adding custom functions and plugins that enable them to take real actions beyond just conversation.

## 📚 What's In This Folder

### 🔧 [02.1 - Azure AI Agents Functions with Foundry SDK Tutorial](02.1-azure_ai_agents_functions_foundry_sdk_tutorial.ipynb)
**Complete guide to adding custom functions using the Azure AI Agents Foundry SDK**

Learn how to extend agent capabilities with the official Azure AI Agents SDK:
- 🎯 Understanding what agent functions are and why they're powerful
- 🔧 Creating and registering custom functions with agents
- 🧮 Building practical examples (calculators, weather, data processing)
- 🔄 Handling function calls and responses in conversations
- 🛠️ Managing function execution and error handling
- 🧹 Best practices for function design and testing

**Perfect for**: Developers who want to add custom capabilities to their agents using Microsoft's official SDK approach.

### 🧠 [02.2 - Azure AI Agents with Semantic Kernel Plugins Tutorial](02.2-azure_ai_agents_semantic_kernel_plugins_tutorial.ipynb)
**Advanced plugin development using Semantic Kernel's plugin architecture**

Explore the sophisticated plugin system of Semantic Kernel:
- 🚀 Enhanced plugin capabilities with Semantic Kernel decorators
- 🔌 Creating reusable plugin classes with `@kernel_function`
- ⚡ Automatic function discovery and parameter handling
- 🎯 Type-safe plugin development with annotations
- 🔄 Advanced plugin patterns and multi-function workflows
- 🏗️ Building plugin libraries for enterprise scenarios

**Perfect for**: Developers who want to leverage Semantic Kernel's advanced plugin architecture for sophisticated agent behaviors.

## 🎯 Learning Path

We recommend following the tutorials in this order:

1. **Start with 02.1** - Master function creation with the Foundry SDK approach
2. **Advance to 02.2** - Explore the enhanced plugin capabilities with Semantic Kernel

**Prerequisites**: Complete the [01-agent-basics](../01-agent-basics/) tutorials first to understand core Azure AI Agents concepts.

## 📋 Prerequisites

Before starting these tutorials, ensure you have:

### Previous Knowledge
- ✅ Completed [01-agent-basics](../01-agent-basics/) tutorials
- ✅ Understanding of Azure AI Agents core concepts
- ✅ Basic Python programming skills

### Azure Resources
- ✅ Azure subscription
- ✅ Azure AI Foundry project
- ✅ Deployed AI model (GPT-4, GPT-3.5-turbo, etc.)

### Environment Setup
- ✅ Python 3.8+ installed
- ✅ Jupyter Notebook or VS Code with notebook support
- ✅ Azure CLI (optional, for authentication)

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

# Optional: For advanced scenarios
REASONING_MODEL_DEPLOYMENT_NAME="your-reasoning-model"
AZURE_SUBSCRIPTION_ID="your-subscription-id"
```

💡 **Tip**: The `.env` file is already present in the project root with example values. Simply update it with your Azure AI project details.

### Required Packages
Each tutorial will install its required packages, but you can install them all upfront:

```bash
pip install azure-ai-agents azure-identity semantic-kernel requests
```

## 🔑 Key Concepts Covered

### 🔧 **Agent Functions vs Plugins**

#### Foundry SDK Functions
- Direct function registration with agents
- Manual function call handling and routing
- Explicit function result processing
- Fine-grained control over function execution
- Perfect for custom workflows and complex logic

#### Semantic Kernel Plugins
- Automatic function discovery through decorators
- Type-safe parameter handling with annotations
- Built-in function calling orchestration
- Plugin-based architecture for reusability
- Enterprise-grade patterns and best practices

### 🛠️ **Function Capabilities**

**What functions enable your agents to do:**
- 🌐 **Access External APIs** (weather, news, databases)
- 🧮 **Perform Calculations** (math, financial, scientific)
- 📊 **Process Data** (analyze files, generate reports)
- 🔍 **Search Information** (web search, document retrieval)
- 📧 **Take Actions** (send emails, create tasks, update systems)

### 💡 **Advanced Patterns**

- **Function Chaining**: Functions that call other functions
- **Conditional Logic**: Smart function selection based on context
- **Error Handling**: Graceful failure and recovery patterns
- **State Management**: Maintaining data across function calls
- **Async Operations**: Non-blocking function execution

## 🚀 Quick Start Guide

### Option 1: Foundry SDK Functions (Direct Control)
```python
from azure.ai.agents import AgentsClient
from azure.ai.agents.models import FunctionTool
from azure.identity import DefaultAzureCredential

# Define your custom function
def get_weather(city: str) -> str:
    """Get weather information for a city."""
    # Your weather API logic here
    return f"Weather in {city}: Sunny, 72°F"

# Create function tool
weather_functions = FunctionTool(functions=[get_weather])

# Create agent with functions
with AgentsClient(
    endpoint=os.environ["PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
) as client:
    agent = client.create_agent(
        model=os.environ["MODEL_DEPLOYMENT_NAME"],
        name="weather-assistant",
        instructions="You help users get weather information.",
        tools=weather_functions.definitions
    )
    
    # Handle conversation with function calls
    # (See tutorial for complete handling logic)
```

### Option 2: Semantic Kernel Plugins (Enhanced)
```python
from semantic_kernel.agents import AzureAIAgent
from semantic_kernel.functions import kernel_function
from azure.identity.aio import DefaultAzureCredential
from typing import Annotated

# Create plugin class
class WeatherPlugin:
    @kernel_function(description="Get weather for a city")
    def get_weather(
        self, 
        city: Annotated[str, "The city name"]
    ) -> Annotated[str, "Weather information"]:
        """Get weather information for a city."""
        return f"Weather in {city}: Sunny, 72°F"

# Create agent with plugin
async with DefaultAzureCredential() as creds:
    client = AzureAIAgent.create_client(
        credential=creds, 
        endpoint=os.environ["PROJECT_ENDPOINT"]
    )
    
    agent = AzureAIAgent(
        client=client,
        definition=await client.agents.create_agent(
            model=os.environ["MODEL_DEPLOYMENT_NAME"],
            name="weather-assistant",
            instructions="You help users get weather information."
        ),
        plugins=[WeatherPlugin()]  # Automatic integration!
    )
    
    # Simple conversation with automatic function calling
    response = await agent.get_response("What's the weather in Seattle?")
```

## 🏗️ What You'll Build

By the end of these tutorials, you'll have built:

### 🧮 **Practical Function Examples**
1. **Calculator Functions** - Basic math operations and complex calculations
2. **Weather Functions** - Real-time weather information retrieval
3. **Text Processing Functions** - Text analysis and manipulation
4. **Random Generators** - Random numbers, passwords, and choices
5. **Date/Time Functions** - Time zone conversions and date calculations

### 🔧 **Advanced Function Patterns**
1. **Multi-Parameter Functions** - Complex input handling
2. **Error-Resilient Functions** - Graceful failure handling
3. **Async Functions** - Non-blocking operations
4. **Plugin Libraries** - Reusable function collections
5. **Production-Ready Patterns** - Enterprise-grade implementations

### 🎯 **Real-World Applications**
1. **API Integrations** - Connect to external services
2. **Data Processing Agents** - Analyze and transform data
3. **Task Automation Agents** - Perform actions on behalf of users
4. **Information Retrieval Agents** - Search and synthesize information
5. **Multi-Modal Agents** - Handle text, images, and files

## 🔍 Troubleshooting

### Common Issues

**Function Not Called**
```
Problem: Agent doesn't use your function
Solutions:
- Verify function name and description are clear
- Check function signature matches expectations
- Test with explicit function requests
- Review agent instructions for function usage guidance
```

**Function Call Errors**
```
Problem: Function execution fails
Solutions:
- Add proper error handling in function code
- Validate all input parameters
- Return meaningful error messages
- Log function calls for debugging
```

**Type Annotation Issues**
```
Problem: Semantic Kernel plugins not working
Solutions:
- Use proper Annotated types for parameters
- Include clear parameter descriptions
- Verify @kernel_function decorator usage
- Check import statements for annotations
```

**Authentication Errors**
```bash
# Make sure you're logged into Azure CLI
az login

# Or set environment variables for service principal
export AZURE_CLIENT_ID="your-client-id"
export AZURE_CLIENT_SECRET="your-client-secret" 
export AZURE_TENANT_ID="your-tenant-id"
```

**Package Installation Issues**
```bash
# Update pip first
pip install --upgrade pip

# Install with verbose output to see any errors
pip install -v azure-ai-agents semantic-kernel requests
```

## 📖 Additional Resources

- [Azure AI Agents Functions Documentation](https://docs.microsoft.com/azure/ai-services/agents/functions/)
- [Semantic Kernel Plugins Documentation](https://learn.microsoft.com/semantic-kernel/plugins/)
- [Function Calling Best Practices](https://docs.microsoft.com/azure/ai-services/openai/function-calling/)
- [Azure AI Foundry Documentation](https://docs.microsoft.com/azure/ai-services/foundry/)

## 🎯 Next Steps

After completing these function and plugin tutorials, explore:

- **[03-orchestrated-agents](../03-orchestrated-agents/)** - Coordinating multiple agents with functions
- **[04-orchestrated-agents-with-tools](../04-orchestrated-agents-with-tools/)** - Advanced tool integration patterns
- **[05-orchestrated-agents-with-custom-openapi-tools](../05-orchestrated-agents-with-custom-openapi-tools/)** - Building custom API integrations

## 💡 Tips for Success

1. **Start Simple** - Begin with basic functions before building complex ones
2. **Test Incrementally** - Test each function individually before integration
3. **Handle Errors Gracefully** - Always include proper error handling
4. **Document Functions** - Use clear descriptions and parameter annotations
5. **Monitor Performance** - Track function execution times and success rates
6. **Security First** - Validate inputs and protect sensitive data
7. **Reuse Code** - Build plugin libraries for common functionality

## 🌟 Function Development Best Practices

### ✅ **Function Design**
- **Single Responsibility**: Each function should do one thing well
- **Clear Naming**: Use descriptive function and parameter names
- **Input Validation**: Always validate and sanitize inputs
- **Error Handling**: Return meaningful error messages
- **Documentation**: Include docstrings and parameter descriptions

### ✅ **Performance Optimization**
- **Caching**: Cache frequently requested data
- **Timeouts**: Set appropriate timeouts for external calls
- **Async Operations**: Use async for I/O-bound operations
- **Resource Management**: Properly close connections and files
- **Rate Limiting**: Respect API rate limits

### ✅ **Security Considerations**
- **Input Sanitization**: Clean and validate all inputs
- **API Key Management**: Use secure credential storage
- **Access Control**: Limit function permissions appropriately
- **Logging**: Log function usage without exposing sensitive data
- **Error Messages**: Don't leak internal system information

---

🎉 **Ready to supercharge your agents with custom functions?** Start with the Foundry SDK tutorial and progress to advanced Semantic Kernel plugins to unlock the full potential of Azure AI Agents!
