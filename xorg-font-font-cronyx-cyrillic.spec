# $Rev: 3204 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	font-cronyx-cyrillic
Summary(pl):	font-cronyx-cyrillic
Name:		xorg-font-font-cronyx-cyrillic
Version:	0.99.0
Release:	0.01
License:	MIT
Group:		X11
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/font/font-cronyx-cyrillic-%{version}.tar.bz2
# Source0-md5:	c046249bcc47d2096dd4f4a379f8949a
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-font-font-util
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/font-cronyx-cyrillic-%{version}-root-%(id -u -n)

%description
font-cronyx-cyrillic

%description -l pl
font-cronyx-cyrillic


%prep
%setup -q -n font-cronyx-cyrillic-%{version}


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
%{_libdir}/X11/fonts/cyrillic/*
