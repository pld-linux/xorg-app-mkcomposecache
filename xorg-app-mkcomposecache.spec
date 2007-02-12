Summary:	mkcomposecache application - create global Compose cache files
Summary(pl.UTF-8):   Aplikacja mkcomposecache - tworzenie globalnych plików cache Compose
Name:		xorg-app-mkcomposecache
Version:	1.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/mkcomposecache-%{version}.tar.bz2
# Source0-md5:	c8237b4aea1ae0c15441deab6b12c5c0
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

%description -l pl.UTF-8
mkcomposecache służy do tworzenia globalnych (ogólnosystemowych)
plików cache Compose.

Pliki cache Compose poprawiają czas uruchamiania aplikacji i
wykorzystanie pamięci, szczególnie przy lokalizacjach z dużymi
tablicami Compose (np. wszystkimi lokalizacjami UTF-8).

%prep
%setup -q -n mkcomposecache-%{version}

%build
%{__aclocal}
%{__autoconf}
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
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_sbindir}/mkcomposecache
%{_mandir}/man8/mkcomposecache.8*
