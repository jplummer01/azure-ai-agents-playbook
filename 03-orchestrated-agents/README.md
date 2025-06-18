# 🎭 Orchestrated Agents - Multi-Agent Coordination

Welcome to the world of multi-agent orchestration! This folder contains comprehensive tutorials that show you how to coordinate multiple Azure AI agents working together to solve complex problems through sophisticated collaboration patterns.

## 📚 What's In This Folder

### 🔄 [03.1 - Concurrent and Sequential Orchestration Tutorial](03.1-concurrent_and_sequential_orchestration_tutorial.ipynb)
**Master the art of multi-agent orchestration with Semantic Kernel**

Learn advanced coordination patterns with specialized agent teams:
- 🎯 Understanding orchestration patterns and when to use them
- 🔄 Sequential orchestration for pipeline workflows (Agent A → Agent B → Agent C)
- ⚡ Concurrent orchestration for parallel processing (A + B + C → Combine)
- 🏗️ Creating specialized agents with domain-specific plugins
- 📊 Performance comparison between orchestration patterns
- 🛠️ Advanced Semantic Kernel orchestration features

**Perfect for**: Developers who want to build sophisticated multi-agent systems that can handle complex workflows through coordinated agent collaboration.

### 🤝 [03.2 - Connected Agents Tutorial](03.2-connected_agents_tutorial.ipynb)
**Learn agent-to-agent communication and hybrid orchestration approaches**

Explore different approaches to agent connectivity and collaboration:
- 🔗 Azure AI Foundry SDK connected agents using ConnectedAgentTool
- 🔌 Semantic Kernel AzureAIAgent plugins for hybrid workflows
- 🎯 Agent specialization and task delegation patterns
- 🔄 Comparison between direct connection vs plugin wrapping
- 🚀 Hybrid workflows combining both SDK approaches
- 💡 Best practices for agent communication architectures

**Perfect for**: Developers who want to understand different agent connection patterns and build systems that leverage both Azure AI Foundry and Semantic Kernel capabilities.

## 🎯 Learning Path

We recommend following the tutorials in this order:

1. **Start with 03.1** - Master orchestration patterns with specialized agent teams
2. **Advance to 03.2** - Learn agent connectivity and hybrid approaches

**Prerequisites**: Complete the [01-agent-basics](../01-agent-basics/) and [02-agent-custom-functions](../02-agent-custom-functions/) tutorials first to understand core concepts and function integration.

## 📋 Prerequisites

Before starting these tutorials, ensure you have:

### Previous Knowledge
- ✅ Completed [01-agent-basics](../01-agent-basics/) tutorials
- ✅ Completed [02-agent-custom-functions](../02-agent-custom-functions/) tutorials
- ✅ Understanding of Azure AI Agents and custom functions/plugins
- ✅ Basic knowledge of async/await patterns in Python

### Azure Resources
- ✅ Azure subscription
- ✅ Azure AI Foundry project
- ✅ Deployed AI model (GPT-4, GPT-3.5-turbo, etc.)
- ✅ Azure OpenAI resource (for Semantic Kernel scenarios)

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

# Required for Semantic Kernel orchestration (03.1)
AZURE_OPENAI_ENDPOINT="https://your-resource.openai.azure.com/"
AZURE_OPENAI_API_KEY="your-openai-api-key"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your-chat-deployment"

# Optional: For advanced scenarios
REASONING_MODEL_DEPLOYMENT_NAME="your-reasoning-model"
AZURE_SUBSCRIPTION_ID="your-subscription-id"
```

💡 **Tip**: The `.env` file is already present in the project root with example values. Simply update it with your Azure AI project details.

### Required Packages
Each tutorial will install its required packages, but you can install them all upfront:

```bash
pip install azure-ai-agents azure-identity semantic-kernel asyncio
```

## 🔑 Key Concepts Covered

### 🎭 **Multi-Agent Orchestration**

**What orchestration enables:**
- 🎯 **Specialization**: Each agent excels in specific domains
- ⚡ **Parallel Processing**: Multiple agents work simultaneously  
- 📈 **Better Results**: Domain experts produce higher quality outputs
- 🔄 **Scalability**: Add more agents as needed
- 💪 **Resilience**: If one agent fails, others continue

### 🔄 **Orchestration Patterns**

#### Sequential Orchestration (Pipeline)
- **Flow**: Agent A → Agent B → Agent C
- **Use Cases**: Document processing, analysis workflows, step-by-step procedures
- **Benefits**: Quality control, context building, dependent task chains
- **Example**: Research Agent → Analytics Agent → Content Agent

#### Concurrent Orchestration (Parallel)
- **Flow**: Agent A + Agent B + Agent C → Combine Results
- **Use Cases**: Independent tasks, multi-source research, parallel processing
- **Benefits**: Speed, efficiency, diverse perspectives
- **Example**: Multiple research agents gathering different data sources

#### Hybrid Patterns
- **Flow**: Mix of sequential and concurrent patterns
- **Use Cases**: Complex workflows with both dependent and independent tasks
- **Benefits**: Optimal performance and quality for complex scenarios

### 🤝 **Agent Connectivity Approaches**

#### Connected Agents (Foundry SDK)
- **Method**: `ConnectedAgentTool` for agent-to-agent communication
- **Pattern**: Agent calls other agents as tools
- **Benefits**: Direct delegation, simple coordination, built-in tool management
- **Use Cases**: Task delegation, specialized function calls

#### AzureAI Plugins (Semantic Kernel)
- **Method**: Wrap Azure AI agents as Semantic Kernel plugins
- **Pattern**: Hybrid SK orchestration with Azure AI power
- **Benefits**: Rich orchestration features, type safety, advanced patterns
- **Use Cases**: Complex workflows, enterprise scenarios, hybrid architectures

### 🏗️ **Advanced Architecture Patterns**

- **Agent Specialization**: Creating domain-expert agents
- **Plugin Libraries**: Reusable agent capabilities
- **Workflow Optimization**: Performance tuning and pattern selection
- **Error Handling**: Resilient multi-agent systems
- **Resource Management**: Efficient agent lifecycle management

## 🚀 Quick Start Guide

### Option 1: Sequential Orchestration (Quality-focused)
```python
from semantic_kernel.agents import SequentialOrchestration, ChatCompletionAgent

# Create specialized agents
research_agent = ChatCompletionAgent(
    name="Dr_Research",
    instructions="You are a research specialist...",
    service=chat_service,
    plugins=[research_plugin]
)

analytics_agent = ChatCompletionAgent(
    name="Prof_Analytics", 
    instructions="You are a data analysis expert...",
    service=chat_service,
    plugins=[analytics_plugin]
)

# Create sequential orchestration
orchestration = SequentialOrchestration(
    members=[research_agent, analytics_agent],
    agent_response_callback=monitor_callback
)

# Execute pipeline workflow
result = await orchestration.invoke(
    task="Analyze market trends in renewable energy",
    runtime=runtime
)
```

### Option 2: Concurrent Orchestration (Speed-focused)
```python
from semantic_kernel.agents import ConcurrentOrchestration

# Create concurrent orchestration with same agents
orchestration = ConcurrentOrchestration(
    members=[research_agent, analytics_agent, content_agent]
)

# Execute parallel workflow
result = await orchestration.invoke(
    task="Multi-perspective analysis of AI in healthcare",
    runtime=runtime
)

# All agents work simultaneously, then combine results
final_results = await result.get(timeout=300)
```

### Option 3: Connected Agents (Direct Communication)
```python
from azure.ai.agents.models import ConnectedAgentTool

# Create specialized agents
stock_agent = client.create_agent(
    model=os.environ["MODEL_DEPLOYMENT_NAME"],
    name="stock_expert",
    instructions="You provide stock price information."
)

# Create connected agent tool
stock_tool = ConnectedAgentTool(
    id=stock_agent.id,
    name="stock_expert", 
    description="Gets stock prices for companies"
)

# Create coordinator that uses connected agents
coordinator = client.create_agent(
    model=os.environ["MODEL_DEPLOYMENT_NAME"],
    name="coordinator",
    instructions="Coordinate with specialist agents.",
    tools=[stock_tool.definitions[0]]
)

# Coordinator automatically calls specialist agents as needed
```

## 🏗️ What You'll Build

By the end of these tutorials, you'll have built:

### 🎭 **Sophisticated Agent Teams**
1. **Research + Analytics + Content Pipeline** - Sequential workflow for comprehensive analysis
2. **Multi-Perspective Analysis System** - Concurrent agents providing diverse insights
3. **Specialized Agent Network** - Domain experts working together
4. **Hybrid Orchestration Systems** - Combining multiple patterns for optimal results

### 🔄 **Advanced Orchestration Patterns**
1. **Pipeline Workflows** - Step-by-step agent processing chains
2. **Parallel Processing** - Simultaneous multi-agent execution
3. **Dynamic Coordination** - Adaptive workflow routing
4. **Error-Resilient Systems** - Graceful failure handling and recovery

### 🤝 **Agent Communication Systems**
1. **Tool-Based Delegation** - Agents calling other agents as tools
2. **Plugin Integration** - Wrapping agents as reusable plugins
3. **Hybrid Architectures** - Combining Foundry SDK and Semantic Kernel
4. **Enterprise Patterns** - Production-ready agent coordination

## 🔍 Troubleshooting

### Common Issues

**Orchestration Timeout Errors**
```
Problem: Agents take too long in orchestration
Solutions:
- Increase timeout values in orchestration.invoke()
- Optimize agent instructions for conciseness
- Check Azure service quotas and performance
- Monitor individual agent response times
```

**Agent Communication Failures**
```
Problem: Connected agents don't respond correctly
Solutions:
- Verify agent IDs are correct in ConnectedAgentTool
- Check agent instructions are clear and specific
- Ensure proper error handling in coordinator logic
- Test individual agents before orchestration
```

**Semantic Kernel Runtime Issues**
```
Problem: InProcessRuntime errors or hangs
Solutions:
- Always call runtime.start() before orchestration
- Use proper cleanup with runtime.stop_when_idle()
- Handle async context managers correctly
- Monitor runtime resource usage
```

**Memory and Performance Issues**
```
Problem: High resource usage with multiple agents
Solutions:
- Limit concurrent agent count based on resources
- Use agent cleanup after orchestration completion
- Monitor Azure AI service consumption
- Implement proper timeout handling
```

**Authentication and Configuration Errors**
```bash
# Make sure you're logged into Azure CLI
az login

# Verify all required environment variables
echo $PROJECT_ENDPOINT
echo $AZURE_OPENAI_ENDPOINT
echo $MODEL_DEPLOYMENT_NAME

# Check Azure OpenAI access for Semantic Kernel
az cognitiveservices account show --name your-openai-resource --resource-group your-rg
```

## 📖 Additional Resources

- [Semantic Kernel Orchestration Documentation](https://learn.microsoft.com/semantic-kernel/agents/)
- [Azure AI Agents Connected Tools Documentation](https://docs.microsoft.com/azure/ai-services/agents/tools/)
- [Multi-Agent Systems Design Patterns](https://docs.microsoft.com/azure/ai-services/patterns/)
- [Azure AI Foundry Orchestration Guide](https://docs.microsoft.com/azure/ai-services/foundry/)

## 🎯 Next Steps

After mastering orchestrated agents, explore:

- **[04-orchestrated-agents-with-tools](../04-orchestrated-agents-with-tools/)** - Adding external tools and APIs to orchestrated workflows
- **[05-orchestrated-agents-with-custom-openapi-tools](../05-orchestrated-agents-with-custom-openapi-tools/)** - Building custom API integrations for agent teams
- **[06-magentic-one-orchestration](../06-magentic-one-orchestration/)** - Advanced multi-agent orchestration patterns

## 💡 Tips for Success

1. **Start with Simple Patterns** - Master sequential before concurrent orchestration
2. **Design for Specialization** - Create agents with clear, focused expertise
3. **Test Individual Agents First** - Ensure each agent works before orchestration
4. **Monitor Performance** - Track execution times and resource usage
5. **Handle Errors Gracefully** - Implement robust error handling and cleanup
6. **Choose the Right Pattern** - Sequential for quality, concurrent for speed
7. **Optimize Instructions** - Keep agent instructions clear and concise

## 🌟 Orchestration Best Practices

### ✅ **Agent Design**
- **Clear Specialization**: Each agent should have a distinct, well-defined role
- **Focused Instructions**: Write specific instructions for each agent's domain
- **Plugin Optimization**: Use specialized plugins that match agent expertise
- **Consistent Naming**: Use descriptive names that reflect agent capabilities

### ✅ **Orchestration Patterns**
- **Pattern Selection**: Choose sequential for dependencies, concurrent for independence
- **Timeout Management**: Set appropriate timeouts for different workflow types
- **Error Recovery**: Implement fallback strategies for failed agents
- **Resource Monitoring**: Track performance and optimize bottlenecks

### ✅ **Production Considerations**
- **Scalability**: Design for horizontal scaling with more agents
- **Monitoring**: Implement comprehensive logging and monitoring
- **Security**: Secure agent-to-agent communication and data handling
- **Cost Management**: Monitor Azure service consumption and optimize usage

### ✅ **Development Workflow**
- **Incremental Building**: Test individual components before orchestration
- **Version Control**: Track agent configurations and orchestration patterns
- **Testing Strategy**: Automated testing for orchestration workflows
- **Documentation**: Document agent roles and orchestration patterns

---

🎉 **Ready to orchestrate sophisticated agent teams?** Start with sequential orchestration patterns and progress to advanced concurrent and hybrid workflows to build truly intelligent multi-agent systems!
