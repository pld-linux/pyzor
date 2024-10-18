#
%bcond_without	doc
#
%define		module pyogg
%define		dver	1-1-2
Summary:	Pyzor - a collaborative system to detect and block spam
Summary(pl.UTF-8):	Pyzor - współpracujący system do wykrywania i blokowania spamu
Name:		pyzor
Version:	1.1.2
Release:	1
License:	GPL v2
Group:		Applications/Mail
Source0:	https://github.com/SpamExperts/pyzor/archive/release-%{dver}.tar.gz
# Source0-md5:	659eca5fe90582b1ac5841a3340f5620
URL:		http://pyzor.org/
BuildRequires:	python3-devel
BuildRequires:	python3-modules
BuildRequires:	rpm-pythonprov
%{?with_doc:BuildRequires:	sphinx-pdg}
Requires:	python3-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collaborative system to detect and block spam.

Pyzor initially started out to be merely a Python implementation of
Razor, but due to the protocol and the fact that Razor's server is not
Open Source or software libre, the author decided to impelement Pyzor
with a new protocol and release the entire system as Open Source and
software libre.

%description -l pl.UTF-8
Współpracujący system do wykrywania i blokowania spamu.

Pyzor początkowo miał być pythonową implementacją Razora, ale z powodu
protokołu i faktu, że serwer Razora nie jest wolnodostępnym
oprogramowaniem z otwartymi źródłami, autor zdecydował się
zaimplementować Pyzora z nowym protokołem i wydać cały system jako
oprogramowanie wolnodostępne z otwartymi źródłami.

%prep
%setup -q -n %{name}-release-%{dver}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst THANKS %{?with_doc:docs/.build/html}
%attr(755,root,root) %{_bindir}/*
%{py3_sitescriptdir}/pyzor
%{py3_sitescriptdir}/pyzor-%{version}-py*.egg-info
