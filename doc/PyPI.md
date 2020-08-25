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

# Troubleshooting

## Trouble installing pygame

Windows installs `pygame` with no problem.

If `pygame` fails to install on Linux Mint, it is because there
are several non-Python dependencies that are missing.

### Install `pygame` build dependencies

`pygame` is a Python wrapper around `SDL` and requires
`sdl-config`.

Install `sdl-config`:

```bash
$ sudo apt install libsdl1.2-dev
```

*The install collects additional packages that are not part of the
default Linux Mint distribution. Proceed with installing the
additional packages.*

Check `sdl-config` is installed:

```bash
$ sdl-config --version
1.2.15
```

Obtain all of the other dependencies for building pygame using
the list of build dependencies for the `python-pygame` package:

```bash
$ sudo apt-get build-dep python-pygame
```

The following dependencies are installed:

```
libflac-dev
libjbig-dev
libjpeg-dev
libjpeg-turbo8-dev
libjpeg8-dev
liblzma-dev
libmad0-dev
libmikmod-config
libmikmod-dev
libogg-dev
libportmidi-dev
libpython-all-dev
libsdl-image1.2-dev
libsdl-mixer1.2-dev
libsdl-ttf2.0-dev
libsmpeg-dev
libtiff-dev
libtiff5-dev
libtiffxx5
libvorbis-dev
libwebp-dev
python-all
pythonall-dev
sharutils
```

Note this is not the same as installing the Linux package
`python-pygame`. These are the packages needed for *building*
`python-pygame`. Luckily, these are also the packages for
`pip` to run pygame's `setup.py`.

Now finally pygame will install with the usual command:

```bash
$ pip install pygame
```

Or:

```bash
$ pip install microspecgui
```

## Trouble running the GUI because it does not see the dev-kit

If the GUI cannot see the dev-kit it is a setup problem with USB.
Windows and Linux each have their own USB setup.

### Enable VCP driver on Windows

The dev-kit uses FTDI# FT221X for USB communication. You should
not need to download drivers from the FTDI site, but you do need
to tell Windows to `Load VCP` for this device.

This setup only has to be done once for the dev-kit, but if you
are using more than one dev-kit you need to do it for each one.

- open Device Manager
- locate `USB Serial Converter`, right-click and select
  `Properties`
- on the `Advanced` tab, check the box to `Load VCP`

### Grant USB permission On Linux Mint

If this user is communicating with an FTDI device over USB
for the first time, you probably need to add this user to the
`dialout` group. This grants the user permission to communicate
with the dev-kit over USB.

This setup only has to be done once for the dev-kit. If you
are using more than one dev-kit, you do not need to do this setup
again.

### Check hardware is visible

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

