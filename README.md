# kmod-clk-mpfs

This package provides a clock driver for Microchip PolarFire SoC baed on <https://patchwork.kernel.org/project/linux-clk/patch/20210107113500.15642-3-daire.mcnamara@microchip.com/>.

# Building packages

1. Prepare an RISC-V developer environment with `qemu-system-riscv64`. For details, refer to <https://fedoraproject.org/wiki/Architectures/RISC-V/Installing>.
2. Clone the repository.
3. Run `rpmbuild`.
    ~~~
    $ cd kmod-clk-mpfs
    $ rpmbuild --define "_topdir $PWD" --define "_sourcedir $PWD" -ba kmod-clk-mpfs.spec 
    ~~~
