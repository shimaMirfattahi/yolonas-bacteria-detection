from super_gradients.training import Trainer
from omegaconf import OmegaConf

cfg = OmegaConf.load("yolonas_train.yaml")
trainer = Trainer(experiment_name=cfg.experiment_name, ckpt_root_dir=cfg.ckpt_root_dir)
trainer.train_from_config(cfg)