Summary:	Optical Character Recognition program
Summary(pl):	Program optycznego rozpoznawania pisma (OCR)
Name:		ocrad
Version:	0.4
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://savannah.nongnu.org/download/ocrad/%{name}-%{version}.tar.bz2
# Source0-md5:	dc477bff7ae0e0cda7490c1f90789338
URL:		http://www.gnu.org/software/ocrad/ocrad.html
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ocrad is an OCR program implemented as a filter. It reads a bitmap
image in pbm format and outputs text in ISO-8859-1 (Latin-1) charset.
It can be used as a stand-alone terminal application, or as a backend
to other programs.

%description -l pl
Ocrad jest programem OCR zaimplementowanym jako filtr. Czyta bitmap� w
formacie pbm i zwraca tekst w zestawie znak�w ISO-8859-1 (Latin-1).
Mo�e by� u�ywany jako samodzielna aplikacja terminalowa b�d� jako
podstawa innego programu.

%prep
%setup -q

%build
./configure \
	--prefix=/usr
%{__make} \
	CXXFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_infodir}}

install ocrad $RPM_BUILD_ROOT%{_bindir}
install ocrad.png $RPM_BUILD_ROOT%{_pixmapsdir}
install doc/ocrad.info $RPM_BUILD_ROOT%{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_infodir}/*
