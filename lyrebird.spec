Name:          lyrebird
Summary:       Simple and powerful voice changer for Linux, written in GTK 3.
URL:           https://github.com/lyrebird-voice-changer/%{name}

Version:       1.1.0
Release:       4%{dist}
License:       MIT

Source0:       %{URL}/archive/v%{version}.tar.gz
BuildArch:     noarch

BuildRequires: gettext

Requires:      python3 >= 3.7.0
Requires:      python3-toml
Requires:      python3-gobject
Requires:      pulseaudio
Requires:      sox

%description
Simple and powerful voice changer for Linux, written in GTK 3.

%prep
%setup -q -n %{name}-%{version}

%install
install -dm 0755 %{buildroot}/%{_bindir}
install -m 0755 %{name} %{buildroot}/%{_bindir}/
install -dm 0755 %{buildroot}/%{_datadir}/%{name}
cp -rf app app.py icon.png %{buildroot}/%{_datadir}/%{name}/
install -dm 0755 %{buildroot}/%{_datadir}/applications
BIN_PATH=%{_bindir} SHARE_PATH=%{_datadir}/%{name} envsubst < %{name}.desktop > %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%license LICENSE
%doc README.md CHANGELOG.md
