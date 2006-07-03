Summary:	mkcomposecache application - create global Compose cache files
Summary(pl):	Aplikacja mkcomposecache - tworzenie globalnych plików cache Compose
Name:		xorg-app-mkcomposecache
Version:	1.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/mkcomposecache-%{version}.tar.bz2
# Source0-md5:	f04e80847eda166c80c7c570ed517cbd
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mkcomposecache is used for creating global (system-wide) Compose cache
files.

Compose cache files help with application startup times and memory
usage, especially in locales with large Compose tables (e.g. all UTF-8
locales).

%description -l pl
mkcomposecache s³u¿y do tworzenia globalnych (ogólnosystemowych)
plików cache Compose.

Pliki cache Compose poprawiaj± czas uruchamiania aplikacji i
wykorzystanie pamiêci, szczególnie przy lokalizacjach z du¿ymi
tablicami Compose (np. wszystkimi lokalizacjami UTF-8).

%prep
%setup -q -n mkcomposecache-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*.8*
