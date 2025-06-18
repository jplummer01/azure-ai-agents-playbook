# Voice Orchestration

🎤 **Build Voice-Enabled AI Agents with Real-Time Audio Processing**

This folder demonstrates how to create voice-controlled Azure AI Agents that can process speech input, understand natural language commands, and perform actions like sending emails through Azure Logic Apps. Learn to build conversational AI systems with real-time voice interaction capabilities.

## 🎯 What You'll Learn

- **Voice-Enabled Agents**: Create agents that respond to spoken commands
- **Real-Time Audio Processing**: Handle live audio streams and speech recognition
- **Azure Logic Apps Integration**: Connect voice agents to business workflows
- **WebSocket Communication**: Implement real-time audio streaming
- **Multi-Modal Interaction**: Combine voice, text, and action capabilities
- **Production Voice Systems**: Build scalable voice-controlled applications

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    Voice Orchestration System                   │
└─────────────────────┬───────────────────────────────────────────┘
                      │
    ┌─────────────────┼─────────────────┬─────────────────┐
    │                 │                 │                 │
┌───▼────┐    ┌──────▼──────┐    ┌─────▼─────┐    ┌─────▼─────┐
│ Audio  │    │   Speech    │    │   Azure   │    │ Logic     │
│Capture │    │Recognition  │    │ AI Agent  │    │ Apps      │
│        │    │             │    │           │    │           │
└───┬────┘    └──────┬──────┘    └─────┬─────┘    └─────┬─────┘
    │                │                 │                │
┌───▼────┐    ┌──────▼──────┐    ┌─────▼─────┐    ┌─────▼─────┐
│ Voice  │    │ WebSocket   │    │ Function  │    │  Email    │
│ Utils  │    │  Stream     │    │   Tools   │    │ Service   │
└────────┘    └─────────────┘    └───────────┘    └───────────┘
```

## 📁 Project Structure

```
07-voice-orchestration/
├── 07.1-voice-email-demo.py      # Voice-controlled email agent demo
├── voice.py                      # Voice processing utilities and AgentVoice class
├── requirements.txt              # Python dependencies for voice processing
├── __pycache__/                  # Python cache files
└── README.md                     # This file
```

## 📚 Components

### 07.1-voice-email-demo.py
**🎤 Voice-Controlled Email Agent**

A complete demonstration of a voice-enabled agent that can:
- **Listen to voice commands** using real-time audio capture
- **Process speech** through Azure Speech Services
- **Execute email tasks** via Azure Logic Apps integration
- **Provide voice feedback** with text-to-speech responses

**Key Features:**
- Real-time voice command processing
- Azure Logic Apps workflow integration
- Email composition and sending via voice
- Multi-modal interaction (voice + text)
- Error handling and user feedback

### voice.py
**🔧 Voice Processing Framework**

Core voice processing utilities including:
- **AgentVoice Class**: Main voice interaction handler
- **Audio Capture**: Real-time microphone input processing
- **WebSocket Streaming**: Efficient audio data transmission
- **Speech Recognition**: Azure Speech Services integration
- **Voice Activity Detection**: Smart conversation flow management

**Key Features:**
- WebSocket-based audio streaming
- Azure Deep Noise Suppression
- Semantic Voice Activity Detection (VAD)
- Audio preprocessing and optimization
- Real-time conversation handling

## 🛠️ Prerequisites

### Required Azure Resources
- **Azure AI Project** with deployed language model
- **Azure Speech Services** resource
- **Azure Logic Apps** (for email functionality)
- **Azure Subscription** with appropriate permissions

### Environment Variables
Configure your environment with the following variables:

```bash
# Azure AI Configuration
PROJECT_ENDPOINT="https://your-ai-project.openai.azure.com/"
MODEL_DEPLOYMENT_NAME="gpt-4o"  # or your deployed model
AZURE_OPENAI_API_KEY="your-api-key"
AZURE_OPENAI_ENDPOINT="https://your-openai.openai.azure.com/"

# Azure Speech Services
AZURE_SPEECH_KEY="your-speech-service-key"
AZURE_SPEECH_REGION="your-speech-region"

# Azure Logic Apps (for email features)
AZURE_SUBSCRIPTION_ID="your-subscription-id"
AZURE_RESOURCE_GROUP_NAME="your-resource-group"
LOGIC_APP_NAME="your-logic-app-name"
```

### Required Python Packages
```bash
pip install azure-ai-agents
pip install azure-identity
pip install azure-mgmt-logic
pip install numpy
pip install sounddevice
pip install websockets
pip install asyncio
pip install aiohttp
```

### System Requirements
- **Microphone**: Hardware microphone for audio input
- **Speakers/Headphones**: Audio output for voice responses
- **Windows/macOS/Linux**: Cross-platform audio support
- **Python 3.8+**: Compatible Python version

## 🚀 Quick Start

### 1. Environment Setup
```bash
# Clone the repository
git clone https://github.com/Azure-Samples/azure-ai-agents-playbook.git
cd azure-ai-agents-playbook/07-voice-orchestration

# Install dependencies
pip install -r requirements.txt

# Set up environment variables (create .env file at project root)
# Add all required environment variables listed above
```

### 2. Configure Azure Logic Apps (Optional)
```bash
# Create a Logic App for email functionality
az logic workflow create \
  --resource-group <your-rg> \
  --name <logic-app-name> \
  --location <region>

# Configure email connector in Logic Apps
# Set up HTTP trigger for agent integration
```

### 3. Run Voice-Enabled Email Agent
```bash
# Start the voice-controlled agent
python 07.1-voice-email-demo.py

# Speak commands like:
# "Send an email to john@example.com about our meeting tomorrow"
# "Check my recent emails"
# "Schedule a follow-up email"
```

## 🧩 Learning Path

### Beginner Level
1. **Audio Basics**: Understand audio capture and processing fundamentals
2. **Speech Recognition**: Learn Azure Speech Services integration
3. **Simple Voice Commands**: Build basic voice-controlled functions

### Intermediate Level
1. **Real-Time Processing**: Implement WebSocket-based audio streaming
2. **Voice Activity Detection**: Add intelligent conversation flow
3. **Multi-Modal Integration**: Combine voice with other input methods

### Advanced Level
1. **Production Voice Systems**: Build scalable voice applications
2. **Custom Voice Models**: Train specialized speech recognition
3. **Enterprise Integration**: Connect to complex business workflows

## 💡 Key Concepts

### Voice Processing Pipeline
1. **Audio Capture**: Real-time microphone input
2. **Preprocessing**: Noise reduction and audio optimization
3. **Speech Recognition**: Convert speech to text
4. **Natural Language Processing**: Extract intent and entities
5. **Action Execution**: Perform requested tasks
6. **Voice Response**: Generate and speak responses

### Real-Time Audio Streaming
- **WebSocket Communication**: Low-latency audio transmission
- **Buffer Management**: Efficient audio data handling
- **Stream Processing**: Real-time audio analysis
- **Quality Control**: Audio quality monitoring and adjustment

### Azure Speech Services Integration
- **Speech-to-Text**: High-accuracy speech recognition
- **Text-to-Speech**: Natural voice synthesis
- **Voice Customization**: Custom voice models and styles
- **Language Support**: Multi-language voice processing

## 🔧 Advanced Configuration

### Custom Voice Settings
```python
# Configure voice processing parameters
voice_config = {
    "sample_rate": 24000,
    "channels": 1,
    "bit_depth": 16,
    "buffer_size": 1024,
    "noise_suppression": True,
    "echo_cancellation": True
}
```

### Speech Recognition Optimization
```python
# Advanced speech recognition settings
speech_config = {
    "language": "en-US",
    "profanity_filter": True,
    "continuous_recognition": True,
    "interim_results": True,
    "timeout": 30000  # 30 seconds
}
```

### Logic Apps Integration
```python
# Configure email workflow
email_workflow = {
    "trigger_url": "https://your-logic-app-url",
    "authentication": "managed_identity",
    "timeout": 60,
    "retry_policy": {
        "type": "exponential",
        "count": 3
    }
}
```

## 🐛 Troubleshooting

### Common Issues

**Audio Device Problems**
```bash
# List available audio devices
python -c "import sounddevice as sd; print(sd.query_devices())"

# Test microphone functionality
python -c "import sounddevice as sd; import numpy as np; print('Recording...'); sd.rec(int(1 * 16000), samplerate=16000, channels=1)"
```

**WebSocket Connection Issues**
```bash
# Check network connectivity
ping your-speech-endpoint.cognitiveservices.azure.com

# Verify authentication
az account show
az cognitiveservices account keys list --name <speech-resource>
```

**Speech Recognition Accuracy**
```bash
# Optimize audio quality
# - Use a high-quality microphone
# - Minimize background noise
# - Speak clearly and at appropriate volume
# - Adjust microphone positioning

# Check speech service quota
az cognitiveservices account show --name <speech-resource> --query "sku"
```

### Performance Optimization

**Audio Latency Reduction**
- Use smaller buffer sizes for real-time processing
- Optimize WebSocket connection parameters
- Implement audio preprocessing on the client side
- Use dedicated audio processing threads

**Recognition Accuracy Improvement**
- Implement custom language models
- Use acoustic adaptation for specific environments
- Add domain-specific vocabulary
- Implement confidence score filtering

## 📊 Best Practices

### Audio Processing
- **Quality First**: Use high-quality audio hardware
- **Noise Management**: Implement noise suppression and filtering
- **Buffer Optimization**: Balance latency and stability
- **Error Handling**: Graceful degradation for audio issues

### Voice User Experience
- **Clear Prompts**: Provide clear voice command guidance
- **Feedback**: Give immediate audio/visual confirmation
- **Error Recovery**: Handle misunderstood commands gracefully
- **Accessibility**: Support various speaking styles and accents

### Production Deployment
- **Scalability**: Design for multiple concurrent users
- **Monitoring**: Track audio quality and recognition accuracy
- **Security**: Secure audio data transmission and storage
- **Compliance**: Ensure privacy and data protection compliance

## 🔒 Security & Privacy

### Audio Data Protection
- **Encryption**: Encrypt audio streams during transmission
- **Minimal Storage**: Avoid storing unnecessary audio data
- **Access Control**: Implement proper authentication
- **Audit Logging**: Track audio processing activities

### Privacy Compliance
- **Consent Management**: Obtain proper user consent
- **Data Retention**: Implement appropriate retention policies
- **Regional Compliance**: Follow local privacy regulations
- **Anonymization**: Remove personally identifiable information

## 📈 Advanced Patterns

### Multi-Language Support
```python
# Dynamic language switching
class MultiLanguageVoiceAgent:
    def __init__(self):
        self.supported_languages = ["en-US", "es-ES", "fr-FR", "de-DE"]
        self.current_language = "en-US"
    
    def switch_language(self, language_code):
        if language_code in self.supported_languages:
            self.current_language = language_code
            self.update_speech_config()
```

### Custom Wake Word Detection
```python
# Implement custom wake word functionality
class WakeWordDetector:
    def __init__(self, wake_words=["hey assistant", "voice agent"]):
        self.wake_words = wake_words
        self.is_listening = False
    
    def detect_wake_word(self, audio_chunk):
        # Custom wake word detection logic
        pass
```

### Voice Analytics
```python
# Track voice interaction metrics
class VoiceAnalytics:
    def track_interaction(self, command, success, latency):
        metrics = {
            "command_type": self.classify_command(command),
            "success_rate": success,
            "response_latency": latency,
            "audio_quality": self.assess_audio_quality()
        }
        self.log_metrics(metrics)
```

## 🔗 Integration Examples

### Email Automation
```python
# Voice-controlled email sending
voice_agent.listen_for_command(
    patterns=["send email to *", "email * about *"],
    action=send_email_via_logic_apps
)
```

### Calendar Management
```python
# Voice-controlled calendar operations
voice_agent.listen_for_command(
    patterns=["schedule meeting *", "check calendar for *"],
    action=manage_calendar_events
)
```

### Task Management
```python
# Voice-controlled task creation
voice_agent.listen_for_command(
    patterns=["create task *", "add to my todo list *"],
    action=create_task_item
)
```

## 📚 Additional Resources

### Documentation
- [Azure Speech Services](https://docs.microsoft.com/azure/cognitive-services/speech-service/)
- [Azure Logic Apps](https://docs.microsoft.com/azure/logic-apps/)
- [WebSocket API Reference](https://docs.microsoft.com/azure/cognitive-services/speech-service/websockets)
- [Audio Processing Best Practices](https://docs.microsoft.com/azure/cognitive-services/speech-service/how-to-audio-content-creation)

### Libraries & Tools
- [SoundDevice Documentation](https://python-sounddevice.readthedocs.io/)
- [WebSockets Library](https://websockets.readthedocs.io/)
- [Azure SDK for Python](https://docs.microsoft.com/python/api/overview/azure/)

### Community & Support
- [Azure Speech Community](https://techcommunity.microsoft.com/t5/azure-ai/ct-p/AzureAI)
- [Python Audio Processing](https://github.com/topics/audio-processing)
- [Voice UI Design Guidelines](https://docs.microsoft.com/azure/cognitive-services/speech-service/voice-assistants)

## 🚀 Next Steps

After mastering voice orchestration, explore:

1. **Multi-Modal Agents**: Combine voice with vision and text
2. **Custom Speech Models**: Train domain-specific recognition
3. **Voice Analytics**: Implement conversation analytics
4. **Enterprise Voice Systems**: Build large-scale voice applications
5. **Conversational AI**: Advanced dialog management systems

---

**Ready to give your agents a voice?** 🎤🤖
