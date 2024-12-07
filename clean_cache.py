import torch
import gc

def print_gpu_memory():
    if torch.cuda.is_available():
        print(f"Total GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.2f} GB")
        print(f"Allocated GPU Memory: {torch.cuda.memory_allocated() / 1e9:.2f} GB")
        print(f"Cached GPU Memory: {torch.cuda.memory_reserved() / 1e9:.2f} GB")
        print(f"Free GPU Memory: {(torch.cuda.get_device_properties(0).total_memory - torch.cuda.memory_allocated()) / 1e9:.2f} GB")

# Clear GPU memory
def aggressive_clear_memory():
    print("Before clearing:")
    print_gpu_memory()
    
    # 1. Delete all variables in global scope that are tensors
    for obj in list(globals()):
        if isinstance(globals()[obj], torch.Tensor):
            del globals()[obj]
    
    # 2. Move model to CPU if it exists and clear its cache
    if 'lora_model' in globals():
        lora_model.cpu()
    if 'pretrained_model' in globals():
        pretrained_model.cpu()
    
    # 3. Clear CUDA cache
    torch.cuda.empty_cache()
    
    # 4. Run garbage collector
    import gc
    gc.collect()
    
    print("\nAfter clearing:")
    print_gpu_memory()


aggressive_clear_memory()