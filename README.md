# Autogen Workshop

Welcome to the Autogen Workshop repository, created by Or Sharon. This project aims to provide a comprehensive introduction to Autogen, a cutting-edge tool for automating code generation tasks. Whether you're interested in enhancing your development workflow, incorporating AI-driven code generation into your projects, or exploring the capabilities of Autogen, this workshop is designed to equip you with the knowledge and skills you need.

## Critical Configuration Instructions: OAI_CONFIG_LIST_SAMPLE

Before running the sample code, it's imperative to carefully review and modify the `OAI_CONFIG_LIST_SAMPLE` file. This file contains essential configurations for connecting to various AI models, including GPT-4 and Azure OpenAI deployments. **Failure to correctly configure this file could result in the sample code not functioning as expected.**

### Steps to Configure:

1. **Modify the Content**: Replace placeholder values (e.g., `<your OpenAI API key here>`, `<your Azure OpenAI deployment name>`) with your actual API keys and deployment names.
2. **Rename the File**: Change the file name from `OAI_CONFIG_LIST_SAMPLE` to `OAI_CONFIG_LIST` to make it recognizable by the sample code.
3. **Version Compatibility**: If you are using `pyautogen v0.1.x` with Azure OpenAI, replace `"base_url"` with `"api_base"` in the configurations. Use `pip list` to verify the installed version of `pyautogen`.
4. **Model Selection**: The default model is set to `gpt-4` due to its compatibility and performance with AutoGen. If you opt for a different model, be prepared to adjust system prompts accordingly, especially for models like `GPT-3.5-turbo` which may not perform as well.

### Important Notes:

- **GPT-4 as Default**: GPT-4 is recommended for its proven effectiveness with AutoGen. Switching to a different model may necessitate significant adjustments to system prompts and could introduce risks related to alignment and safety.
- **Caution with Non-OpenAI or Azure Models**: Utilizing models outside of OpenAI or Azure's offerings could pose additional risks. Exercise caution and thoroughly evaluate any such models before integration.

This configuration is critical for the successful operation of the sample code. Please ensure all steps are followed meticulously to avoid any issues.

## Getting Started

Follow these steps to get started with the Autogen Workshop:

1. **Prerequisites**: Ensure you have Python 3.8+, Docker, and Git installed on your system.
2. **Installation**: Clone this repository to your local machine using the command:
```git clone https://github.com/orsharon7/autogen-workshop.git```
3. **Setup**: After cloning, navigate to the repository directory and install the required dependencies:
```pip install -r requirements.txt```


For detailed setup instructions, please refer to the [Official Getting Started](https://microsoft.github.io/autogen/docs/Getting-Started) guide.

## Workshop Overview

The workshop is currently in the design phase. It will feature modules covering various aspects of Autogen, from basic introductions to advanced code generation techniques. Stay tuned for updates on module availability and content.

## Resources

- **Autogen GitHub Repository**: [https://github.com/microsoft/autogen](https://github.com/microsoft/autogen)
- **Getting Started Guide**: [https://microsoft.github.io/autogen/docs/Getting-Started](https://microsoft.github.io/autogen/docs/Getting-Started)
- **LLM Configuration Guide**: [https://microsoft.github.io/autogen/docs/topics/llm_configuration/](https://microsoft.github.io/autogen/docs/topics/llm_configuration/)
- **Examples**: [https://microsoft.github.io/autogen/docs/Examples/](https://microsoft.github.io/autogen/docs/Examples/)

## About the Creator

Or Sharon is the creator of the Autogen Workshop. For more information about Or and his work, visit his [LinkedIn profile](https://www.linkedin.com/in/orsharon/).

## Contributing

Contributions to the Autogen Workshop are welcome! If you have suggestions for improvement, discover a bug, or wish to add more examples, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.