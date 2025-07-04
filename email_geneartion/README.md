# CrewAI Email Generation System

An intelligent email generation system powered by [CrewAI](https://crewai.com) that automatically creates professional emails from document content and user topics. This multi-agent AI system uses document analysis and email composition agents to craft contextually appropriate emails.

## 🚀 Features

- **Document Analysis**: Automatically extracts key information from `.txt`, `.pdf`, and `.docx` files
- **Intelligent Email Generation**: Creates professional, context-aware emails based on document content
- **Multi-Agent Collaboration**: Uses specialized AI agents for document analysis and email composition
- **Automatic Email Sending**: Integrates with Gmail to send generated emails automatically
- **Support for Multiple Formats**: Handles various document types with appropriate parsing

## 📋 Requirements

- Python >=3.10 <3.14
- Google Gemini API key
- Gmail app password (for email sending)

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd crewai-email-generation/email_geneartion
   ```

2. **Install UV (if not already installed)**:
   ```bash
   pip install uv
   ```

3. **Install dependencies**:
   ```bash
   uv sync
   ```

4. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```bash
   MODEL=gemini/gemini-1.5-flash
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## 🔧 Configuration

### Getting API Keys

1. **Google Gemini API Key**:
   - Go to [Google AI Studio](https://aistudio.google.com/)
   - Create a new project or select an existing one
   - Generate an API key
   - Add it to your `.env` file

2. **Gmail App Password** (for email sending):
   - Enable 2-factor authentication on your Gmail account
   - Go to Google Account settings > Security > App passwords
   - Generate a new app password
   - Use this password when prompted during email sending

### Document Preparation

Place your documents in the `docs/` folder or provide the full path when prompted. Supported formats:
- `.txt` - Plain text files
- `.pdf` - PDF documents
- `.docx` - Microsoft Word documents

## 🎯 Usage

### Basic Usage

1. **Run the email generation system**:
   ```bash
   crewai run
   ```

2. **Follow the prompts**:
   - Enter the topic/subject for your email
   - Provide the path to your document (e.g., `docs/leave_request.txt`)
   - Enter recipient's email address
   - Enter your Gmail address
   - Enter your Gmail app password

3. **Generated output**:
   - The system will analyze your document
   - Create a professional email
   - Save it as `generated_email.txt`
   - Automatically send it via Gmail

### Example Workflow

```bash
$ crewai run
Running the Crew
Enter the info you want to send an email about:
➤ Leave request for medical reasons

Enter path to the document (e.g., docs/info.txt):
➤ docs/leave_request.txt

Enter recipient's email address:
➤ hr@company.com

Enter your Gmail address:
➤ your.email@gmail.com

Enter your 16-character Gmail app password:
➤ your_app_password
```

## 🤖 AI Agents

### Document Analyst Agent
- **Role**: Intelligent Document Analyst
- **Goal**: Extract key information from document content
- **Skills**: Document parsing, information extraction, context understanding

### Email Writer Agent
- **Role**: Professional Email Generator
- **Goal**: Create polished, context-aware emails
- **Skills**: Professional writing, email formatting, tone adjustment

## 📁 Project Structure

```
email_geneartion/
├── src/
│   └── email_geneartion/
│       ├── __init__.py
│       ├── main.py              # Main application entry point
│       ├── crew.py              # CrewAI agent and task definitions
│       ├── doc_reader.py        # Document parsing utilities
│       ├── email_sender.py      # Email sending functionality
│       ├── config/
│       │   ├── agents.yaml      # Agent configurations
│       │   └── tasks.yaml       # Task definitions
│       └── tools/
│           ├── __init__.py
│           └── custom_tool.py   # Custom tools for agents
├── docs/                        # Document storage
├── knowledge/                   # Knowledge base
├── tests/                       # Test files
├── pyproject.toml              # Project configuration
├── uv.lock                     # Dependency lock file
├── .env                        # Environment variables
└── README.md                   # This file
```

## 🔍 Troubleshooting

### Common Issues

1. **"API key not valid" error**:
   - Verify your Gemini API key is correct in `.env`
   - Ensure the API key has proper permissions

2. **"No module named 'yagmail'" error**:
   - Run `uv sync` to install all dependencies
   - Ensure virtual environment is activated

3. **Document reading errors**:
   - Check file path is correct
   - Verify file format is supported (.txt, .pdf, .docx)
   - Ensure file is not corrupted

4. **Email sending failures**:
   - Verify Gmail app password is correct
   - Check internet connection
   - Ensure 2-factor authentication is enabled

### Performance Tips

- Use clear, well-structured documents for better analysis
- Provide specific topics for more focused email generation
- Keep documents under 10MB for optimal processing

## 🛡️ Security

- Never commit your `.env` file to version control
- Use app passwords instead of your main Gmail password
- Regularly rotate your API keys
- Review generated emails before sending

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [CrewAI](https://crewai.com)
- Powered by Google Gemini AI
- Document parsing with PyPDF2 and python-docx
- Email sending via yagmail

## 📞 Support

For questions or issues:
- Check the [CrewAI documentation](https://docs.crewai.com)
- Open an issue on the [GitHub repository](https://github.com/joaomdmoura/crewai)
- Review the troubleshooting section above
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
