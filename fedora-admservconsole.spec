# http://directory.fedora.redhat.com/wiki/BuildingConsole#Building_Fedora_Admin_Server_Console
Summary:	Fedora Admin Server Java Remote Management Console
Summary(pl.UTF-8):   Konsola w Javie do zdalnego zarządzania serwerem Fedora Admin Server
Name:		fedora-admservconsole
# don't update to 1.1 (unless it's really 1.1; sources from 20060620 are really 1.0.2)
Version:	1.0.3
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://directory.fedora.redhat.com/sources/%{name}-%{version}.tar.gz
# Source0-md5:	b5f05aa3d8b3b38a858ccbda6ac014f0
Patch0:		%{name}-path.patch
URL:		http://directory.fedora.redhat.com/wiki/Client_software
BuildRequires:	ant
BuildRequires:	fedora-console >= 1.0
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	ldapsdk >= 4.17
BuildRequires:	rpmbuild(macros) >= 1.294
Requires:	fedora-console >= 1.0
Requires:	ldapsdk >= 4.17
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fedora Admin Server Java Remote Management Console.

%description -l pl.UTF-8
Konsola w Javie do zdalnego zarządzania serwerem Fedora Admin Server.

%prep
%setup -q
%patch0 -p1

%build
%ant \
	-Dconsole.location=%{_datadir}/fedora-console \
	-Dldapjdk.location=%{_javadir} \
	-Dadmservconsole.root=`pwd`

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

install built/package/fedora-admserv-%{version}.jar $RPM_BUILD_ROOT%{_datadir}/%{name}
install built/package/fedora-admserv-%{version}_en.jar $RPM_BUILD_ROOT%{_datadir}/%{name}

ln -sf fedora-admserv-%{version}.jar $RPM_BUILD_ROOT%{_datadir}/%{name}/fedora-admserv-1.0.jar
ln -sf fedora-admserv-%{version}_en.jar $RPM_BUILD_ROOT%{_datadir}/%{name}/fedora-admserv-1.0_en.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/fedora-admserv-%{version}.jar
%{_datadir}/%{name}/fedora-admserv-%{version}_en.jar
%{_datadir}/%{name}/fedora-admserv-1.0.jar
%{_datadir}/%{name}/fedora-admserv-1.0_en.jar
