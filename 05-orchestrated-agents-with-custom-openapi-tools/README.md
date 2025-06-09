# Orchestrated Agents with Custom OpenAPI Tools

🏦 **Learn how to connect Azure AI Agents to your own custom FastAPI services!**

This project demonstrates how to create Azure AI Agents that can interact with custom FastAPI services through OpenAPI specifications. You'll learn to build, deploy, and integrate custom APIs with intelligent agents that can understand and process business data.

## 🎯 What You'll Learn

- **FastAPI Development**: Create RESTful APIs with automatic OpenAPI spec generation
- **Azure AI Agents Integration**: Connect agents to custom APIs using OpenAPI tools
- **Local & Cloud Deployment**: Run services locally and deploy to Azure Container Apps
- **Real-world Use Cases**: Build agents that interact with banking transaction data

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Azure AI      │    │   Custom FastAPI │    │   Azure         │
│   Agents        │◄──►│   Service        │    │   Container     │
│                 │    │                  │    │   Apps          │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                       │                       │
         │              ┌────────▼────────┐             │
         └─────────────►│  OpenAPI Spec   │◄────────────┘
                        │  /openapi.json  │
                        └─────────────────┘
```

## 📁 Project Structure

```
05-orchestrated-agents-with-custom-openapi-tools/
├── 05.1-fastapi_openapi_tutorial.ipynb    # Main tutorial notebook
├── bank_transactions_api.py                # FastAPI service implementation
├── Dockerfile                             # Container configuration
├── aci_requirements.txt                   # Python dependencies
├── azure.yaml                            # Azure Developer CLI configuration
├── README.md                             # This file
├── infra/                                # Infrastructure as Code
│   ├── main.bicep                        # Main Bicep template
│   ├── main.parameters.json              # Configuration parameters
│   └── modules/                          # Modular Bicep templates
│       ├── acr-build.bicep              # Container Registry build
│       ├── app.bicep                    # Container App configuration
│       ├── container-apps.bicep         # Container Apps Environment
│       ├── container-registry.bicep     # Azure Container Registry
│       ├── monitoring.bicep             # Log Analytics workspace
│       └── uami.bicep                   # User Assigned Managed Identity
└── arm/                                  # ARM template for one-click deploy
    └── main.json                        # ARM template
```

## 🚀 Quick Start

### Option 1: One-Click Azure Deployment

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure-Samples%2Fazure-ai-agents-playbook%2Fmain%2F05-orchestrated-agents-with-custom-openapi-tools%2Farm%2Fmain.json)

### Option 2: Azure Developer CLI (Recommended)

```bash
# Clone the repository
git clone https://github.com/Azure-Samples/azure-ai-agents-playbook.git
cd azure-ai-agents-playbook/05-orchestrated-agents-with-custom-openapi-tools

# Deploy with Azure Developer CLI
azd up

# Show the environment variables
azd env get-values
```

### Option 3: Local Development

```bash
# Install dependencies
pip install -r aci_requirements.txt

# Run the FastAPI service locally
python bank_transactions_api.py 8000

# Open another terminal and run the Jupyter notebook
jupyter notebook 05.1-fastapi_openapi_tutorial.ipynb
```

## 📋 Prerequisites

### Required Azure Resources
- **Azure AI Project** with deployed language model
- **Azure Container Registry** (created automatically)
- **Azure Container Apps Environment** (created automatically)
- **Azure Log Analytics Workspace** (created automatically)

### Environment Variables
Set these environment variables before running the tutorial:

```bash
export PROJECT_ENDPOINT="https://your-ai-project.openai.azure.com/"
export MODEL_DEPLOYMENT_NAME="gpt-4o"  # or your deployed model name
```

### Required Python Packages
```
azure-ai-agents
azure-identity
semantic-kernel
fastapi
uvicorn
requests
```

## 🛠️ Features

### 🏦 Bank Transactions API
- **GET /transactions**: Retrieve latest bank transactions
- **GET /transactions/{id}**: Get specific transaction details
- **GET /openapi.json**: OpenAPI specification endpoint
- **Automatic Documentation**: FastAPI generates interactive docs at `/docs`

### 🤖 Azure AI Agent Capabilities
- **OpenAPI Integration**: Automatically consume FastAPI endpoints
- **Natural Language Queries**: Ask questions about financial data in plain English
- **Intelligent Responses**: Get insights, summaries, and categorized spending analysis
- **Real-time Data**: Connect to live API endpoints for current information

## 📖 Tutorial Walkthrough

The `05.1-fastapi_openapi_tutorial.ipynb` notebook provides a step-by-step guide:

1. **🔧 Setup and Prerequisites** - Environment configuration and requirements
2. **🚀 Start FastAPI Service** - Launch the bank transactions API
3. **🧪 Test API Endpoints** - Verify the service is working correctly
4. **📋 Fetch OpenAPI Spec** - Retrieve the API specification dynamically
5. **🤖 Create Azure AI Agent** - Build an agent with OpenAPI tools
6. **💬 Interactive Testing** - Query the agent with natural language
7. **🛑 Cleanup** - Stop services and clean up resources

## 💡 Example Use Cases

### Financial Assistant
```python
# Agent can answer questions like:
"Show me my latest bank transactions and tell me how much I spent on food."
"What was my largest expense recently and what category was it in?"
"Can you give me a summary of my account balance and recent activity?"
```

### API Integration Patterns
- **Microservices Integration**: Connect agents to existing business APIs
- **Data Analysis**: Enable conversational queries over structured data
- **Workflow Automation**: Create agents that can trigger business processes
- **Real-time Monitoring**: Build agents that monitor and report on system status

## 🔧 Configuration

### FastAPI Service Configuration
The `bank_transactions_api.py` includes:
- Sample transaction data
- RESTful endpoints with proper HTTP methods
- Automatic OpenAPI spec generation
- CORS configuration for cross-origin requests
- Error handling and validation

### Azure Infrastructure
The Bicep templates create:
- **Container Registry**: For storing container images
- **Container Apps Environment**: Managed container hosting
- **Log Analytics**: For monitoring and diagnostics
- **User Assigned Managed Identity**: For secure resource access

## 🚦 Deployment Options

### Local Development
```bash
# Start FastAPI service
python bank_transactions_api.py 8000

# Service available at: http://localhost:8000
# API docs at: http://localhost:8000/docs
# OpenAPI spec at: http://localhost:8000/openapi.json
```

### Azure Container Apps
```bash
# Deploy with azd
azd up

# Check deployment status
azd env get-values

# View logs
az containerapp logs show --name <app-name> --resource-group <rg-name>
```


## 🔒 Security Considerations

### Production Deployment
- **Authentication**: Implement proper API authentication (JWT, OAuth2, etc.)
- **HTTPS**: Ensure all API communications use TLS
- **Rate Limiting**: Implement request throttling to prevent abuse
- **Input Validation**: Validate all API inputs thoroughly
- **Secrets Management**: Use Azure Key Vault for sensitive configuration

### Development Security
- **Environment Variables**: Never commit secrets to version control
- **Network Security**: Use Azure Private Endpoints for production deployments
- **RBAC**: Implement proper role-based access control

## 🐛 Troubleshooting

### Common Issues

**FastAPI Service Won't Start**
```bash
# Check if port is already in use
netstat -an | grep :8000

# Try a different port
python bank_transactions_api.py 8001
```

**Azure AI Agent Connection Issues**
```bash
# Verify environment variables
echo $PROJECT_ENDPOINT
echo $MODEL_DEPLOYMENT_NAME

# Check Azure authentication
az account show
```

**Container Deployment Failures**
```bash
# Check container logs
az containerapp logs show --name <app-name> --resource-group <rg-name>

# Verify container registry access
az acr list --query "[].{Name:name,LoginServer:loginServer}"
```

## 📚 Additional Resources

- [Azure AI Agents Documentation](https://docs.microsoft.com/azure/ai-services/agents/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [OpenAPI Specification](https://swagger.io/specification/)
- [Azure Container Apps Documentation](https://docs.microsoft.com/azure/container-apps/)
- [Azure Developer CLI](https://docs.microsoft.com/azure/developer/azure-developer-cli/)

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](../CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

---

## 🎯 Next Steps

After completing this tutorial, consider exploring:

- **Authentication Integration**: Add OAuth2 or JWT authentication to your APIs
- **Database Integration**: Connect your FastAPI service to Azure SQL or Cosmos DB
- **Multiple Agents**: Create orchestrated agents that work together
- **Production Deployment**: Deploy to Azure with proper monitoring and scaling
- **Advanced OpenAPI**: Explore complex OpenAPI specifications with multiple services

**Happy coding!** 🚀