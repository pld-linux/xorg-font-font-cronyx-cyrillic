Summary:	Cronyx Cyrillic bitmap fonts
Summary(pl.UTF-8):	Fonty bitmapowe Cronyx w cyrylicy
Name:		xorg-font-font-cronyx-cyrillic
Version:	1.0.1
Release:	1
License:	distributable (see COPYING)
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-cronyx-cyrillic-%{version}.tar.bz2
# Source0-md5:	15f86f5e572df21218617982eb4b3bfc
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/cyrillic
# contains useful aliases for these fonts
Requires:	xorg-font-font-alias >= 1.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cronyx Cyrillic bitmap fonts: Courier, Helvetica, Times, Fixed and
Nil.

%description -l pl.UTF-8
Fonty bitmapowe Cronyx w cyrylicy: Courier, Helvetica, Times, Fixed i
Nil.

%prep
%setup -q -n font-cronyx-cyrillic-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--build=%{_host_platform} \
	--host=%{_host_platform} \
	--with-fontdir=%{_fontsdir}/cyrillic

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst cyrillic

%postun
fontpostinst cyrillic

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_fontsdir}/cyrillic/crox*.pcf.gz
%{_fontsdir}/cyrillic/koi*.pcf.gz
