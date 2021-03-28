%bcond_without check
%global debug_package %{nil}

%global crate tinyvec_macros

Name:           rust-%{crate}
Version:        0.1.0
Release:        1%{?dist}
Summary:        Some macros for tiny containers

# Upstream license specification: MIT OR Apache-2.0 OR Zlib
License:        MIT OR Apache-2.0 OR Zlib
URL:            https://crates.io/crates/tinyvec_macros
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Some macros for tiny containers.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(tinyvec_macros) = 0.1.0
Requires:       cargo

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(tinyvec_macros/default) = 0.1.0
Requires:       cargo
Requires:       crate(tinyvec_macros) = 0.1.0

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
