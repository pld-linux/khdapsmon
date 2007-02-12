Summary:	Monitor primarily for the Hard Drive Active Protection System (HDAPS)
Summary(pl.UTF-8):   Monitorowanie systemu aktywnej ochrony dysku twardego (HDAPS)
Name:		khdapsmon
Version:	0.1.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.oakcourt.dyndns.org/projects/khdapsmon/%{name}_%{version}-2.tar.gz
# Source0-md5:	5f6a63492329785abe38716c43b28a19
URL:		http://www.oakcourt.dyndns.org/projects/khdapsmon/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6.1
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
# needed for actual protection, but khdapsmon doesn't use hpadsd in any way
Requires:	hdapsd
# relies on kernel hdaps driver, which depends on CONFIG_X86
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
khdapsmon is a monitor primarily for the Hard Drive Active Protection
System (HDAPS) found in IBM ThinkPads. It's primary interface is a
system tray icon that indicates whether the queue is frozen or not on
the selected hard disk device. This is similar to the tray icon found
on the pre-installed OS on ThinkPads. It could work with other
systems similar to the ThinkPad's, such as those found in Apple
PowerBooks but this has not been tested and is dependent upon some
code that is not yet available. A status dialog also prints out useful
information like accelerometer status and keyboard/mouse activity
status. It also allows for the selection of the monitored device if
you have more than one hard disk that supports queue freezing.

%description -l pl.UTF-8
khdapsmon to monitor przeznaczony głównie dla systemu HDAPS (Hard
Drive Active Protection System - systemu aktywnej ochrony dysku
twadego), jaki można spotkać w notebookach IBM ThinkPad. Główny
interfejs to ikona zasobnika systemowego określająca, czy kolejka
operacji jest zamrożona dla wybranego dysku twardego. Jest podobna do
ikony paska w systemie operacyjnym preinstalowanym na ThinkPadach.
Mogłoby to działać z systemami podobnymi do tego w ThinkPadzie, jak
na przykład tym obecnym w Apple PowerBookach, ale nie było to
testowane i wymaga to kodu, który nie został jeszcze napisany. Okno
dialogowe stanu wypisuje różne przydatne informacje, takie jak stan
czujnika przyspieszenia oraz aktywności klawiatury i myszy. Pozwala
także na wybór monitorowanego urządzenia, jeśli dostępny jest więcej
niż jeden dysk twardy obsługujący zamrażanie kolejki.

%prep
%setup -q

%build
cp %{_datadir}/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
	--%{!?debug:dis}%{?debug:en}able-debug \
	%{!?debug:--disable-rpath} \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{name}    --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kde/khdapsmon.desktop
%{_datadir}/apps/khdapsmon
%{_iconsdir}/*/*/*/*.png
