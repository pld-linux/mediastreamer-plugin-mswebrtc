# TODO: system webrtc?
Summary:	WebRTC plugin for mediastreamer
Summary(pl.UTF-8):	Wtyczka WebRTC dla mediastreamera
Name:		mediastreamer-plugin-mswebrtc
Version:	1.1.2
Release:	2
License:	GPL v2
Group:		Libraries
#Source0Download: https://gitlab.linphone.org/BC/public/mswebrtc/-/tags
Source0:	https://gitlab.linphone.org/BC/public/mswebrtc/-/archive/%{version}/mswebrtc-%{version}.tar.bz2
# Source0-md5:	2a6434473876a79b904b19706f6c16c1
%define	webrtc_gitref	583acd27665cfadef8ab03eb85a768d308bd29dd
Source1:	https://gitlab.linphone.org/BC/public/external/webrtc/-/archive/%{webrtc_gitref}/webrtc-%{webrtc_gitref}.tar.bz2
# Source1-md5:	2eb3cb36b5728dc7c841b73ad4a66761
Patch0:		%{name}-make.patch
Patch1:		%{name}-link.patch
Patch2:		mswebrtc-sse2.patch
Patch3:		mswebrtc-cmake.patch
Patch4:		mswebrtc-b64-refactor.patch
URL:		https://gitlab.linphone.org/BC/public/mswebrtc
BuildRequires:	cmake >= 3.1
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	mediastreamer-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
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
%{__tar} xf %{SOURCE1} -C webrtc --strip-components=1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
# autotools suite is more outdated, doesn't have VAD support
install -d builddir
cd builddir
%cmake .. \
	-DENABLE_STATIC=OFF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C builddir install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/mediastreamer/plugins/libmswebrtc.so*
