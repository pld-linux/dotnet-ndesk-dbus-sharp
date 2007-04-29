# TODO: noarch or optflags
#
%include	/usr/lib/rpm/macros.mono
#
Summary:	.NET library for using D-BUS message bus
Summary(pl.UTF-8):	Biblioteka .NET do używania magistrali przesyłania komunikatów D-BUS
Name:		ndesk-dbus
Version:	0.4.2
Release:	0.1
License:	MIT
Group:		Libraries
Source0:	http://www.ndesk.org/archive/dbus-sharp/dbus-sharp-%{version}.tar.gz
# Source0-md5:	b858011c167c6bc318dcb4d6383996be
Patch0:		ndesk-dbus-gac_dir.patch
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
%setup -q -n dbus-sharp-%{version}
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C src install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/NDesk.DBus
