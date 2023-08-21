Name:          lyrebird
Summary:       Simple and powerful voice changer for Linux, written in GTK 3.
Version:       1.2.0
Release:       1
License:       MIT
Group:         Sound
URL:           https://github.com/lyrebird-voice-changer/%{name}
Source0:       %{URL}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:     noarch

BuildRequires: gettext

Requires:      python
Requires:      python3dist(toml)
Requires:      python-gobject3
Requires:      (pipewire or pulseaudio)
Requires:      sox
Requires:      pulseaudio-utils

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
