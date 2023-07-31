import julia
from julia.api import Julia

def setup(compiled_modules=True):
    julia.install()
    jl = Julia(compiled_modules=compiled_modules)

    from julia import Pkg
    Pkg.add(url="https://github.com/op3/AngularCorrelation.jl.git")
