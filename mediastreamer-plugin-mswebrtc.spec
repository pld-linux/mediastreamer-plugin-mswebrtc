# TODO: system webrtc?
Summary:	WebRTC plugin for mediastreamer
Summary(pl.UTF-8):	Wtyczka WebRTC dla mediastreamera
Name:		mediastreamer-plugin-mswebrtc
Version:	1.1.1
Release:	3
License:	GPL v2
Group:		Libraries
#Source0Download: https://gitlab.linphone.org/BC/public/mswebrtc/-/tags
#Source0:	https://gitlab.linphone.org/BC/public/mswebrtc/-/archive/%{version}/mswebrtc-%{version}.tar.bz2
Source0:	https://linphone.org/releases/old/sources/plugins/mswebrtc/mswebrtc-%{version}.tar.gz
# Source0-md5:	9f70eb5e5448dc8eaaaf72be13fe740c
Patch0:		%{name}-make.patch
Patch1:		%{name}-link.patch
URL:		https://gitlab.linphone.org/BC/public/mswebrtc
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRequires:	mediastreamer-devel >= 2.0.0
BuildRequires:	pkgconfig
Requires:	mediastreamer >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package supplies the mediastreamer plugin to include features
from WebRTC (iSAC codec, AECM...).

%description -l pl.UTF-8
Ten pakiet udostępnia wtyczkę mediastreamera do funkcji WebRTC (kodek
iSAC, AECM...).

%prep
%setup -q -n mswebrtc-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
# strict means -Werror, there are some "defined but not used" warnings
%configure \
	--disable-strict

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/mediastreamer/plugins/libmswebrtc.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/mediastreamer/plugins/libmswebrtc.so*
