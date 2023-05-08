import torch
from torchvision import transforms as tt

WANDB_LOGIN = False

# dataset preprocessing configs
LOAD_IN_MEMORY = False
DATASET_PATH = "./cats"
DEVICE = 'cpu'
TRANSFORM = tt.Compose([
    tt.ToTensor(),
    tt.Resize(32),
])

# training configs
TRAIN_PORTION = 0.6
VALIDATION_PORTION = 0.2
BATCH_SIZE = 8
N_POPULATION = 32
P_CHILDREN = 0.5
EPOCHS_GA = 3
EPOCHS_INDIVIDUAL = 2

EPOCHS_BEST = 100

# genetic algorithm details
ACTIVATION_FUNCTIONS = ['relu', 'lrelu']
LINEAR_FEATURES = [192, 256, 384, 512, 768, 1024, 1536, 2048, 4096, 8192]
USE_CONV = True
CONV_FEATURES = [3, 4, 8, 12, 16, 24, 32]
KERNEL_SIZES = [3, 5]
LATENT_SIZE = 128
BEST_MODEL_PATH = "./results/best_model.pth"

# output path
GENERATED_PATH = "./results/best.png"
