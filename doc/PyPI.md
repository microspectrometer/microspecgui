# Install

```bash
$ pip install microspecgui
```

This installs:

- `pygame`: Python interface for SDL (Simple DirectMedia Layer),
  a highly portable library for low-level access to graphics
  hardware and input devices (keyboard/mouse/joystick)
- `pygstuff`: helpers to simplify `pygame` applications
- `microspeclib`: Chromation's spectrometer dev-kit API

# Run

Connect the Chromation spectrometer dev-kit, then:

```bash
$ microspec-gui
```

## Keyboard Controls

```
q   - quit
a   - auto-expose (spacebar works also)
x   - decrease exposure time
X   - increase exposure time
h/l - navigate wavelength slow
j/k - navigate wavelength fast
0   - go to shortest wavelength
$   - go to longest wavelength
```

## Joystick Controls

```
BACK - quit
A    - auto-expose
X    - decrease exposure
Y    - increase exposure
right-stick   - navigate wavelength slow
left-stick    - navigate wavelength fast
left-trigger  - go to shortest wavelength
right-trigger - go to longest wavelength
```

# Platform compatibility
Developed on Windows using Python3.8 and `pygame 1.9.6`. Tested
on:

- Windows 8
- Windows 10
- Linux Mint 19.3
- Raspberry Pi OS Lite on:
    - Raspberry Pi v1.2 Model B+ 512MB (2014) -- GUI is slow
    - Raspberry Pi 3 Model B+ (2017) -- GUI is good (like the desktops)


## Trouble installing pygame on Linux

Windows installs the pygame package with no trouble, but Debian
distributions (e.g., Linux Mint and Raspberry Pi OS) are usually
missing SDL build dependencies and are therefore unable to run
pygame out of the box. For example, on Raspberry Pi OS Lite, I
get this error when attempting to `pip install pygame` (or
when attempting to install `microspecgui`, which in turn installs
`pygame`):

```bash
ImportError: libSDL-1.2.so.0: cannot open shared object file: No such file or directory
```

This is easy to fix. There are two steps: update the package
manager with source distributions, then install the pygame
build-dependencies.

### Configure the source list

First, if you have never built anything from source on your Linux
system, you need to configure your package manager source list
with `deb-src` URLs.

The `sources.list` file usually has both `deb` URLs and `deb-src`
URLs, but the `deb-src` ones are commented out. The package
manager needs these sources for installing build dependencies.

Open `/etc/apt/sources.list` and find the lines starting
with `deb-src` that are commented out. Uncomment these lines.

*sources.list is a protected file, so you will need to prefix
your text editor command with `sudo`.*

```bash
sudo vi /etc/apt/sources.list
```

For example, my Linux Mint `/etc/apt/sources.list` has this line:

```list
# deb-src http://archive.ubuntu.com/ubuntu bionic-updates/main amd64 Packages
```

I remove the comment:

```list
deb-src http://archive.ubuntu.com/ubuntu bionic-updates/main amd64 Packages
```

Similarly, on Raspberry Pi OS Lite, there is only one line
starting with `# deb-src`. Uncomment by erasing the `#` symbol,
and save the file.

### Update the package manager with the new sources

Now do `apt update` or `apt-get update` to update the newly
configured sources.

```bash
sudo apt update
```

### Install SDL dependencies

Now install the SDL build dependencies:

```bash
sudo apt-get build-dep python-pygame
```

Note this does not install the python-pygame package, but
installs the dependencies for that package, which is exactly
what's needed to `pip install pygame`.

## Install microspecgui

Now finally microspecgui will install with the usual command:

```bash
$ pip install microspecgui
```

### Build from source

Unrelated to using `pygame` or `microspecgui`, your Debian system
is now empowered to build projects from source, for example:

```bash
sudo apt-get build-dep vim # powerful text editor
```

*This only installs the necessary build dependencies. To actually
install Vim, clone the official repository and follow the
instructions to run the configure and build scripts.*

Installing software with `sudo apt install` is much faster than
building from source. But often, the Debian version is
considerably older than the latest stable version.

For example, at the time of this writing, I ran into this with
both Python and Vim, where the available Debian versions were
considerably older and missing features I relied on. When this
happens, I build from source.

# Trouble running the GUI because it does not see the dev-kit

If the GUI cannot see the dev-kit it is a setup problem with USB.
Windows and Linux each have their own USB setup.

## Enable VCP driver on Windows

The dev-kit uses FTDI# FT221X for USB communication. You should
not need to download drivers from the FTDI site, but you do need
to tell Windows to `Load VCP` for this device.

This setup only has to be done once for the dev-kit, but if you
are using more than one dev-kit you need to do it for each one.

- open Device Manager
- locate `USB Serial Converter`, right-click and select
  `Properties`
- on the `Advanced` tab, check the box to `Load VCP`

## Grant USB permission On Linux Mint

If this user is communicating with an FTDI device over USB
for the first time, you probably need to add this user to the
`dialout` group. This grants the user permission to communicate
with the dev-kit over USB.

This setup only has to be done once for the dev-kit. If you
are using more than one dev-kit, you do not need to do this setup
again.

## Check hardware is visible

- connect the dev-kit with a USB cable
    - *expect:* dev-kit indicator LEDs light up
    - two yellow LEDs
    - three green LEDs
- display messages from the kernel ring buffer that contain
  string `FTDI`:

```bash
$ dmesg | grep FTDI
[101038.609497] usb 3-1: FTDI USB Serial Device converter now attached to ttyUSB0
```

Check if the current user is part of the `dialout` group:

```bash
$ groups $USER | grep dialout
```

If the user is already part of `dialout`, a list of groups is
printed and `dialout` is highlighted.

If the user is not part of `dialout`, nothing is printed.

Add this user to `dialout`:

```bash
$ sudo adduser $USER dialout
```

Confirm the user is part of the `dialout` group:

```bash
$ groups $USER | grep dialout
```

Finally, logout and log back in (or simply restart the computer).
Even though the user is listed as a member of `dialout`, this
change does not take effect until the user logs back in.

