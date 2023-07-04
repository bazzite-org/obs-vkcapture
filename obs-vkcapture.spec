Name:           obs-vkcapture
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        OBS plugin for Vulkan/OpenGL game capture on Linux
License:        GPL-2.0-or-later
URL:            https://github.com/KyleGospo/obs-vkcapture

VCS:            {{{ git_dir_vcs }}}
Source:         {{{ git_dir_pack }}}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  vulkan-devel
BuildRequires:  obs-studio-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  glslang-devel
BuildRequires:  wayland-devel
BuildRequires:  pkgconfig(x11)

%description
OBS plugin for Vulkan/OpenGL game capture on Linux.
Requires OBS >= 27. On X11 you need to explicitly enable EGL: OBS_USE_EGL=1 obs

%package -n libobs_vkcapture
Summary:        Vulkan game capture plugin for OBS Studio
Provides:       libobs_vkcapture = %{version}
Version:        %{version}

%description -n libobs_vkcapture
OBS plugin for Vulkan/OpenGL game capture on Linux

%package -n libobs_glcapture
Summary:        OpenGL game capture plugin for OBS Studio
Provides:       libobs_glcapture = %{version}
Version:        %{version}

%description -n libobs_glcapture
OBS plugin for Vulkan/OpenGL game capture on Linux

%prep
{{{ git_dir_setup_macro }}}

%build
%cmake -DCMAKE_INSTALL_PREFIX=/usr .. \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build %{?_smp_mflags}

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/obs-gamecapture
%{_bindir}/obs-glcapture
%{_bindir}/obs-vkcapture
%{_libdir}/obs-plugins/linux-vkcapture.so
%dir %{_datadir}/obs/obs-plugins/linux-vkcapture/
%{_datadir}/obs/obs-plugins/linux-vkcapture/*
%dir %{_datadir}/vulkan/implicit_layer.d/
%{_datadir}/vulkan/implicit_layer.d/obs_vk*.json

%files -n libobs_vkcapture
%{_libdir}/libVkLayer_obs_vkcapture.so

%files -n libobs_glcapture
%{_libdir}/libobs_glcapture.so

%changelog
{{{ git_dir_changelog }}}
