Name:    kmod-clk-mpfs
Version: 5.5.0
Release: 0.rc5.git0.1.1.riscv64.fc32
Summary: Clock driver for Microchip PolarFire SoC
License: GPLv2
URL:     https://patchwork.kernel.org/project/linux-clk/patch/20210107113500.15642-3-daire.mcnamara@microchip.com/

Source0: clk-mpfs.c
Source1: microchip,mpfs-clock.h
Source2: Makefile

BuildArch: riscv64

BuildRequires: kernel-devel = %{version}-%{release}
BuildRequires: gcc(riscv-64)
BuildRequires: xz

Requires: kernel-modules-uname-r = %{version}-%{release}.%{_arch}
Requires: kernel-uname-r = %{version}-%{release}.%{_arch}

%description
This package provides clock driver for Microchip PolarFire SoC based on posted patch sets.

%prep
mkdir -p kmod-clk-mpfs
cp %SOURCE0 %SOURCE1 %SOURCE2 kmod-clk-mpfs/

%build
cd kmod-clk-mpfs
make -C /usr/src/kernels/%{version}-%{release}.%{_arch}/ M=$PWD

%install
mkdir -p %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/extra/drivers/clk/microchip/
install -p -m 0644 kmod-clk-mpfs/clk-mpfs.ko %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/extra/drivers/clk/microchip/
xz %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/extra/drivers/clk/microchip/clk-mpfs.ko

%files
/lib/modules/%{version}-%{release}.%{_arch}/extra/drivers/clk/microchip/clk-mpfs.ko.xz

%post
/sbin/depmod -a %{version}-%{release}.%{_arch}

%postun
/sbin/depmod -a %{version}-%{release}.%{_arch}

%changelog
* Mon Feb 22 2021 Takayuki Nagata <takayuki-nagata@users.noreply.github.com> 5.5.0-0.rc5.git0.1.1.riscv64.fc32
- kmod-clk-mpfs for kernel-5.5.0-0.rc5.git0.1.1.riscv64.fc32
