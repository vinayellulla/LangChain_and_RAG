from huggingface_hub import model_info

models = [
    "Qwen/Qwen2.5-7B-Instruct",
    "Qwen/Qwen2.5-7B-Instruct-1M",
    "Qwen/Qwen2.5-Coder-32B-Instruct",
    "openai/gpt-oss-120b",
]

for model_name in models:

    print("\n" + "=" * 70)
    print(model_name)

    try:
        info = model_info(
            model_name,
            expand="inferenceProviderMapping"
        )

        mappings = info.inference_provider_mapping

        if not mappings:
            print("❌ No providers found")
            continue

        print("✅ Providers:")

        for provider in mappings:
            print(
                f"Provider: {provider.provider}\n"
                f"Status: {provider.status}\n"
                f"Provider model ID: {provider.provider_id}\n"
                f"Task: {provider.task}\n"
            )

    except Exception as e:
        print("❌ Error:", e)