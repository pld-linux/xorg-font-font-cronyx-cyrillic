Summary:	cronyx-cyrillic font
Summary(pl):	Font cronyx-cyrillic
Name:		xorg-font-font-cronyx-cyrillic
Version:	1.0.0
Release:	0.1
License:	distributable (see COPYING)
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/font/font-cronyx-cyrillic-%{version}.tar.bz2
# Source0-md5:	22b451e7230b8c003cfc496ee2d360cc
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/cyrillic
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cronyx-cyrillic font.

%description -l pl
Font cronyx-cyrillic.

%prep
%setup -q -n font-cronyx-cyrillic-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
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
%{_fontsdir}/cyrillic/*.pcf.gz
