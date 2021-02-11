# Copyright 2021 (c) anonymous-4989 - All Rights Reserved
#

from gpytorch import means
from gpytorch.models import ExactGP

from gpytorch.distributions import MultivariateNormal


class ExactGPModel(ExactGP):
    def __init__(self, train_x, train_y, likelihood, kernel):
        super(ExactGPModel, self).__init__(train_x, train_y, likelihood)
        self.mean_module = means.ConstantMean()
        self.covar_module = kernel

    def forward(self, x):
        mean_x = self.mean_module(x)
        covar_x = self.covar_module(x)
        return MultivariateNormal(mean_x, covar_x)
