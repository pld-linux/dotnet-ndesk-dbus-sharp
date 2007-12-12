# TODO: noarch or optflags
#
%include	/usr/lib/rpm/macros.mono
#

%define  module ndesk-dbus
Summary:	.NET library for using D-BUS message bus
Summary(pl.UTF-8):	Biblioteka .NET do używania magistrali przesyłania komunikatów D-BUS
Name:		dotnet-ndesk-dbus-sharp
Version:	0.6.0
Release:	0.1
License:	MIT
Group:		Libraries
Source0:	http://www.ndesk.org/archive/dbus-sharp/%{module}-%{version}.tar.gz
# Source0-md5:	5157ba105c9ac491f6e900bc78d1791f
URL:		http://www.ndesk.org/DBusSharp
BuildRequires:	mono-csharp >= 1.1.7
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
.NET library for using D-BUS.

%description -l pl.UTF-8
Biblioteka .NET do używania D-BUS.

%prep
%setup -q -n %{module}-%{version}

%build
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
%{_libdir}/mono/ndesk-dbus-1.0
%{_libdir}/mono/gac/NDesk*
%{_pkgconfigdir}/ndesk-dbus-1.0.pc
