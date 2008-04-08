Summary:	Optical Character Recognition program
Summary(pl.UTF-8):	Program optycznego rozpoznawania pisma (OCR)
Name:		ocrad
Version:	0.17
Release:	1
License:	GPL v3+
Group:		Applications/Graphics
Source0:	http://ftp.gnu.org/gnu/ocrad/%{name}-%{version}.tar.bz2
# Source0-md5:	687c213b3334d5a6c2dcef97805c5882
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/ocrad/ocrad.html
BuildRequires:	help2man
BuildRequires:	libstdc++-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ocrad is an OCR program implemented as a filter. It reads a bitmap
image in pbm format and outputs text in ISO-8859-1 (Latin-1) charset.
It can be used as a stand-alone terminal application, or as a backend
to other programs.

%description -l pl.UTF-8
Ocrad jest programem OCR zaimplementowanym jako filtr. Czyta bitmapę w
formacie pbm i zwraca tekst w zestawie znaków ISO-8859-1 (Latin-1).
Może być używany jako samodzielna aplikacja terminalowa bądź jako
podstawa innego programu.

%prep
%setup -q
%patch0 -p1

%build
# not autoconf-generated
./configure \
	--prefix=%{_prefix}
%{__make} all doc \
	CXX="%{__cxx}" \
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

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_infodir}/*.info*
