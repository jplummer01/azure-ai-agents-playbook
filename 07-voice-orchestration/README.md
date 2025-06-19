# 🎤 Voice Orchestration - Voice-Enabled Azure AI Agents

Welcome to the exciting world of voice-controlled AI agents! This folder contains comprehensive tutorials that show you how to create sophisticated voice-enabled Azure AI Agents that can listen, understand, and respond to spoken commands while performing real-world actions through Azure services.

## 📚 What's In This Folder

### 🎤 [07.1 - Voice-Controlled Email Agent Demo](07.1-voice-email-demo.py)
**Complete voice-enabled agent with email automation capabilities**

Learn how to build production-ready voice agents:
- 🔊 Real-time speech recognition and processing
- 🎯 Natural language understanding from voice commands  
- 📧 Email automation through Azure Logic Apps integration
- 🗣️ Voice feedback with text-to-speech responses
- 🌐 WebSocket-based audio streaming for low latency
- 🛠️ Voice processing utilities and best practices

**Perfect for**: Developers who want to add voice capabilities to their AI agents and build conversational systems that can take real actions.

### 🔧 [Voice Processing Framework](voice.py)
**Core voice processing utilities and AgentVoice class**

Explore the sophisticated voice processing infrastructure:
- 🎙️ AgentVoice class for complete voice interaction handling
- 📡 WebSocket-based real-time audio streaming
- 🧠 Azure Speech Services integration with advanced features
- 🔇 Voice Activity Detection (VAD) for smart conversation flow
- 🎛️ Audio preprocessing and noise suppression
- ⚡ Async operations for responsive voice interactions

**Perfect for**: Developers who want to understand the underlying voice processing architecture and build custom voice-enabled applications.

## 🎯 Learning Path

We recommend exploring the components in this order:

1. **Start with voice.py** - Understand the voice processing framework and core utilities
2. **Run 07.1-voice-email-demo.py** - Experience a complete voice-enabled agent in action

**Prerequisites**: Complete the [01-agent-basics](../01-agent-basics/), [02-agent-custom-functions](../02-agent-custom-functions/), and [04-orchestrated-agents-with-tools](../04-orchestrated-agents-with-tools/) tutorials to understand core agent concepts and Logic Apps integration.

## � Prerequisites

Before starting these tutorials, ensure you have:

### Previous Knowledge
- ✅ Completed [01-agent-basics](../01-agent-basics/) tutorials
- ✅ Completed [02-agent-custom-functions](../02-agent-custom-functions/) tutorials  
- ✅ Understanding of Azure Logic Apps from [04-orchestrated-agents-with-tools](../04-orchestrated-agents-with-tools/)
- ✅ Basic knowledge of audio processing concepts

### Azure Resources
- ✅ Azure subscription
- ✅ Azure AI Foundry project
- ✅ Deployed AI model (GPT-4, GPT-3.5-turbo, etc.)
- ✅ Azure Speech Services resource
- ✅ Azure Logic Apps (for email functionality)

### Environment Setup
- ✅ Python 3.8+ installed
- ✅ Microphone and speakers/headphones
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
# Required for voice orchestration
PROJECT_ENDPOINT="https://your-foundry-resource.services.ai.azure.com/api/projects/your-project-name"
MODEL_DEPLOYMENT_NAME="your-model-deployment-name"

# Azure Speech Services (Required)
AZURE_VOICE_LIVE_API_KEY="your-speech-service-key"
AZURE_VOICE_LIVE_REGION="your-speech-region"
AZURE_VOICE_LIVE_ENDPOINT="https://your-cognitive-services.cognitiveservices.azure.com/"

# Azure Logic Apps (for email features)
AZURE_SUBSCRIPTION_ID="your-subscription-id"
AZURE_RESOURCE_GROUP_NAME="your-resource-group"

# Optional: Additional Azure AI configuration
AZURE_OPENAI_API_KEY="your-api-key"
AZURE_OPENAI_ENDPOINT="https://your-openai-resource.openai.azure.com/"
```

💡 **Tip**: The `.env` file is already present in the project root with example values. Simply update it with your Azure AI project details.

### Required Packages
Each tutorial will install its required packages, but you can install them all upfront:

```bash
pip install azure-ai-agents azure-identity azure-mgmt-logic numpy sounddevice websockets python-dotenv
```

### System Requirements
- **Audio Hardware**: Working microphone and speakers/headphones
- **Network**: Stable internet connection for real-time audio streaming
- **Platform**: Windows/macOS/Linux with audio device support

## � Key Concepts Covered

### 🎤 **Voice-Enabled AI Agents**

**What voice capabilities enable:**
- 🗣️ **Natural Interaction**: Speak to agents in natural language
- 🔄 **Multi-Modal Communication**: Combine voice, text, and actions
- ⚡ **Real-Time Processing**: Immediate voice command response
- 🤖 **Hands-Free Operation**: Control agents without typing
- 🎯 **Contextual Understanding**: Maintain conversation context across voice interactions

### 🔧 **Voice Processing Architecture**

#### Audio Capture and Processing
- **Real-Time Streaming**: Continuous audio capture from microphone
- **Quality Enhancement**: Noise suppression and audio optimization
- **Buffer Management**: Efficient audio data handling for low latency
- **Format Conversion**: Audio format standardization for processing

#### Speech Recognition Integration
- **Azure Speech Services**: Enterprise-grade speech-to-text conversion
- **WebSocket Streaming**: Low-latency real-time audio transmission
- **Language Support**: Multi-language speech recognition capabilities
- **Custom Models**: Domain-specific speech recognition optimization

#### Voice Activity Detection (VAD)
- **Smart Listening**: Detect when user starts and stops speaking
- **Conversation Flow**: Natural turn-taking in voice conversations
- **Background Noise Filtering**: Ignore non-speech audio
- **Timeout Management**: Handle pauses and silence appropriately

### 🏗️ **Integration Patterns**

#### Azure Services Integration
- **Speech Services**: Real-time speech recognition and synthesis
- **AI Agents**: Intelligent response generation and task execution
- **Logic Apps**: Automated workflow triggered by voice commands
- **Cognitive Services**: Enhanced audio processing capabilities

#### Application Architecture
- **Event-Driven Processing**: Respond to voice events asynchronously
- **State Management**: Maintain conversation context across interactions
- **Error Handling**: Graceful degradation for audio/recognition issues
- **Security**: Secure audio transmission and data protection

## 🏗️ What You'll Build

By the end of these tutorials, you'll have built:

### 🎤 **Voice-Controlled Email Agent**
- Complete voice interaction system with speech recognition
- Email automation through Azure Logic Apps
- Natural language command processing
- Voice feedback and confirmation system

### � **Voice Processing Framework**  
- Reusable AgentVoice class for any voice-enabled application
- WebSocket-based real-time audio streaming
- Advanced voice activity detection and conversation management
- Integration patterns for Azure Speech Services

### 💡 **Production-Ready Patterns**
- Error handling and graceful degradation
- Audio quality optimization and noise suppression  
- Secure voice data transmission and processing
- Scalable voice agent architectures

## 🎯 Voice Agent Capabilities

**Example voice commands your agents will understand:**
- 📧 *"Send an email to sarah@company.com about the quarterly review"*
- � *"Schedule a meeting with the team for next Tuesday"*  
- 📊 *"Generate a report on last month's sales data"*
- 🔍 *"Search for documents related to the new product launch"*
- ⚙️ *"Update my task list with the items we discussed"*

## 🛠️ Advanced Voice Features

### Real-Time Audio Processing
- Low-latency WebSocket streaming for immediate response
- Continuous audio capture with intelligent buffering
- Background noise suppression and audio enhancement
- Multi-channel audio support for complex environments

### Intelligent Conversation Management  
- Voice Activity Detection (VAD) for natural turn-taking
- Context retention across multi-turn voice conversations
- Interruption handling and conversation recovery
- Timeout management for natural conversation flow

### Enterprise Integration Patterns
- Azure Logic Apps automation triggered by voice
- Multi-modal interfaces combining voice, text, and visual
- Custom speech models for domain-specific terminology
- Voice authentication and speaker identification
