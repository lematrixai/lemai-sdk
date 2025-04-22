from setuptools import setup, find_packages

setup(
    name="lemai-sdk",
    version="0.1.0",
    description="Multi-provider AI chat SDK (OpenAI, Gemini, Custom)",
    author="Erick Lema",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "openai>=1.0.0",
        "requests>=2.28.0",
        "python-dotenv>=1.0.0",
    ],
    python_requires=">=3.7",
)
