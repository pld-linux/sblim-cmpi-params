Summary:	SBLIM CMPI Linux Kernel Parameter instrumentation
Summary(pl.UTF-8):	Przyrządy pomiarowe parametrów jądra Linuksa dla SBLIM CMPI
Name:		sblim-cmpi-params
Version:	1.3.0
Release:	2
License:	Eclipse Public License v1.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
# Source0-md5:	f210fd73d26346c9dc8d2944c1aa9a44
URL:		http://sblim.sourceforge.net/
BuildRequires:	sblim-cmpi-base-devel
BuildRequires:	sblim-cmpi-devel
Requires:	sblim-cmpi-base
Requires:	sblim-sfcb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SBLIM CMPI providers for Linux kernel parameters that are accessible
under subdirs of /proc/sys/.

%description -l pl.UTF-8
Dostawcy informacji SBLIM CMPI dla parametrów jądra Linuksa dostępnych
w podkatalogach /proc/sys/.

%prep
%setup -q

%build
%configure \
	CIMSERVER=sfcb \
	PROVIDERDIR=%{_libdir}/cmpi \
	--disable-static

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

# modules
%{__rm} $RPM_BUILD_ROOT%{_libdir}/cmpi/lib*.la
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_datadir}/%{name}/provider-register.sh \
	-r %{_datadir}/%{name}/Linux_{ABI,FileSystem,Kernel,Network{Core,IPv4,Unix},VirtualMemory}Parameter.registration \
	-m %{_datadir}/%{name}/Linux_{ABI,FileSystem,Kernel,Network{Core,IPv4,Unix},VirtualMemory}Parameter.mof >/dev/null

%preun
if [ "$1" = "0" ]; then
	%{_datadir}/%{name}/provider-register.sh -d \
		-r %{_datadir}/%{name}/Linux_{ABI,FileSystem,Kernel,Network{Core,IPv4,Unix},VirtualMemory}Parameter.registration \
		-m %{_datadir}/%{name}/Linux_{ABI,FileSystem,Kernel,Network{Core,IPv4,Unix},VirtualMemory}Parameter.mof >/dev/null
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog DEBUG NEWS README README.TEST kernel-params
%attr(755,root,root) %{_libdir}/cmpi/libLinux_ABIParameter.so
%attr(755,root,root) %{_libdir}/cmpi/libLinux_FileSystemParameter.so
%attr(755,root,root) %{_libdir}/cmpi/libLinux_KernelParameter.so
%attr(755,root,root) %{_libdir}/cmpi/libLinux_NetworkCoreParameter.so
%attr(755,root,root) %{_libdir}/cmpi/libLinux_NetworkIPv4Parameter.so
%attr(755,root,root) %{_libdir}/cmpi/libLinux_NetworkUnixParameter.so
%attr(755,root,root) %{_libdir}/cmpi/libLinux_VirtualMemoryParameter.so
%dir %{_datadir}/sblim-cmpi-params
%{_datadir}/sblim-cmpi-params/Linux_ABIParameter.mof
%{_datadir}/sblim-cmpi-params/Linux_ABIParameter.registration
%{_datadir}/sblim-cmpi-params/Linux_FileSystemParameter.mof
%{_datadir}/sblim-cmpi-params/Linux_FileSystemParameter.registration
%{_datadir}/sblim-cmpi-params/Linux_KernelParameter.mof
%{_datadir}/sblim-cmpi-params/Linux_KernelParameter.registration
%{_datadir}/sblim-cmpi-params/Linux_NetworkCoreParameter.mof
%{_datadir}/sblim-cmpi-params/Linux_NetworkCoreParameter.registration
%{_datadir}/sblim-cmpi-params/Linux_NetworkIPv4Parameter.mof
%{_datadir}/sblim-cmpi-params/Linux_NetworkIPv4Parameter.registration
%{_datadir}/sblim-cmpi-params/Linux_NetworkUnixParameter.mof
%{_datadir}/sblim-cmpi-params/Linux_NetworkUnixParameter.registration
%{_datadir}/sblim-cmpi-params/Linux_VirtualMemoryParameter.mof
%{_datadir}/sblim-cmpi-params/Linux_VirtualMemoryParameter.registration
%attr(755,root,root) %{_datadir}/sblim-cmpi-params/provider-register.sh
