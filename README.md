# python-angularcorrelation

Python bindings for [AngularCorrelation.jl](https://github.com/op3/AngularCorrelation.jl).

A package to calculate angular distributions and correlations for γ cascades.
The direction and polarization of the zeroth γ-ray are known.
It is aligned with the z axis, the xz plane is the plane of (linear) polarization.

## Installation

Using pip:

```bash
pip install https://github.com/op3/python-angularcorrelation/archive/main.zip
```

## Conventions

The Integral over the complete probability distribution
( ∫∫∫∫ Wcorr(θ₁, ϕ₁,θ₂, ϕ₂) sin(θ₁) sin(θ₂) dθ₁ dφ₁ dθ₂ dφ₂ and
∫∫ W(θ, ϕ) sin(θ) dθ dφ )
is equal to 4π.
Thus, if the direction of the first or second γ is fixed,
one obtains an angular distribution for the other γ.

The KSW convention by Krane, Steffen, Wheeler [\[2\]](#ref-2) for the multipole mixing ratio δ is used.
It is assumed that only the first and second-order multipolarities contribute.

## License<a name="license"></a>

© O. Papst [`<opapst@ikp.tu-darmstadt.de>`](mailto:opapst@ikp.tu-darmstadt.de)

python-angularcorrelation is distributed under the terms of the GNU General Public License, version 3 or later.
See the [`LICENSE`](LICENSE) file.

## Acknowledgments

This work has been funded by the State of Hesse under the grant “Nuclear Photonics” within the LOEWE program.
