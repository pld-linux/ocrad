Summary:	Optical Character Recognition program
Summary(pl.UTF-8):	Program optycznego rozpoznawania pisma (OCR)
Name:		ocrad
Version:	0.21
Release:	1
License:	GPL v3+
Group:		Applications/Graphics
Source0:	http://ftp.gnu.org/gnu/ocrad/%{name}-%{version}.tar.lz
# Source0-md5:	09b09a5f6d5a23551f744ba492e9382e
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/ocrad/ocrad.html
BuildRequires:	help2man
BuildRequires:	libstdc++-devel
BuildRequires:	lzip
BuildRequires:	tar >= 1:1.22
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

%package devel
Summary:	Ocrad static library and header file
Summary(pl.UTF-8):	Biblioteka statyczna i plik nagłówkowy Ocrada
Group:		Development/Libraries
# doesn't require base

%description devel
Ocrad static library and header file.

%description devel -l pl.UTF-8
Biblioteka statyczna i plik nagłówkowy Ocrada.

%prep
%setup -q
%patch0 -p1

%build
# not autoconf-generated
./configure \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}
%{__make} all doc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install ocrad.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/ocrad
%{_pixmapsdir}/ocrad.png
%{_mandir}/man1/ocrad.1*
%{_infodir}/ocrad.info*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libocrad.a
%{_includedir}/ocradlib.h
