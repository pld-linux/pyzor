%define		module pyogg
Summary:	Pyzor - a collaborative system to detect and block spam
Summary(pl):	Pyzor - wsp�pracuj�cy system do wykrywania i blokowania spamu
Name:		pyzor
Version:	0.4.0
Release:	2
License:	GPL
Group:		Networking/Mail
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	ee7afe4cc9d419bce5f29250a01c4374
Patch0:		%{name}-handle_digest_is_none.patch
Patch1:		%{name}-handle_unknown_encoding.patch
Patch2:		%{name}-python_path.patch
URL:		http://pyzor.sourceforge.net/
BuildRequires:	python-devel
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

%description -l pl
Wsp�pracuj�cy system do wykrywania i blokowania spamu.

Pyzor pocz�tkowo mia� by� pythonow� implementacj� Razora, ale z powodu
protoko�u i faktu, �e serwer Razora nie jest wolnodost�pnym
oprogramowaniem z otwartymi �r�d�ami, autor zdecydowa� si�
zaimplementowa� Pyzora z nowym protoko�em i wyda� ca�y system jako
oprogramowanie wolnodost�pne z otwartymi �r�d�ami.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS THANKS UPGRADING docs/*
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitedir}/pyzor
%{py_sitedir}/pyzor/*.py[co]
