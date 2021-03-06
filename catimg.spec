Name:           catimg
Version:        2.2.1
Release:        1%{?dist}
Summary:        Print images in a terminal with 256 colors support

License:        MIT
URL:            https://github.com/posva/catimg
Source0:        https://github.com/posva/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc

%description
%{name} is a little program written in C with no dependencies that prints
images in terminal. It supports JPEG, PNG and GIF formats.

%prep
%autosetup

%build
mkdir -p build
pushd build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo ..
%make_build
popd

%install
pushd build
%make_install
popd

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
