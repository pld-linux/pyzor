#
%bcond_without	doc
#
%define		module pyogg
%define		dver	1-0-0
Summary:	Pyzor - a collaborative system to detect and block spam
Summary(pl.UTF-8):	Pyzor - współpracujący system do wykrywania i blokowania spamu
Name:		pyzor
Version:	1.0.0
Release:	1
License:	GPL v2
Group:		Applications/Mail
Source0:	https://github.com/SpamExperts/pyzor/archive/release-%{dver}.tar.gz
# Source0-md5:	82b351cbf7594974240d655e2e98f20c
URL:		http://pyzor.org/
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%{?with_doc:BuildRequires:	sphinx-pdg}
Requires:	python-modules
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
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/pyzor/*.py
rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/pyzor/*/*.py

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
%dir %{py_sitescriptdir}/pyzor
%{py_sitescriptdir}/pyzor/*.py[co]
%dir %{py_sitescriptdir}/pyzor/engines
%{py_sitescriptdir}/pyzor/engines/*.py[co]
%dir %{py_sitescriptdir}/pyzor/hacks
%{py_sitescriptdir}/pyzor/hacks/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/pyzor-%{version}-py*.egg-info
%endif
