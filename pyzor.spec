%define		module pyogg
Summary:	Pyzor - a collaborative system to detect and block spam
Summary(pl.UTF-8):	Pyzor - współpracujący system do wykrywania i blokowania spamu
Name:		pyzor
Version:	0.5.0
Release:	2
License:	GPL v2
Group:		Applications/Mail
Source0:	http://downloads.sourceforge.net/pyzor/%{name}-%{version}.tar.bz2
# Source0-md5:	21f5ed92470ab12a7658cc46bf59a3e9
URL:		http://pyzor.sourceforge.net/
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
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
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/pyzor/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README THANKS UPGRADING docs/*
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitescriptdir}/pyzor
%{py_sitescriptdir}/pyzor/*.py[co]
