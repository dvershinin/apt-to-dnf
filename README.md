# DO NOT USE< NOTHING TO SEE HERE NOW :-)

# apt-to-dnf

`apt` CLI interface for RPM based distros.

## Audience

* New users of CentOS/RHEL, who only have Ubuntu/Debian experience and want to learn how to use `dnf` as quick as possible, or simply want to run "`apt`"
* Old users of Ubuntu/Debian who are seeing CentOS so "hard", despite the only cruicial difference: `apt` vs `dnf`

# TODOs

We should accept any invalid arguments that `apt` user will specify, which are unknown to `dnf`,
and subsequently only map "in" known arguments:

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-y') # or --yes or  --assume-yes, while --force-yes or -y
# TODO map that to "--assumeyes" in `yum`
args, unknown = parser.parse_known_args(['--foo', 'BAR', 'spam'])
print(args)
# Namespace(foo='BAR')
print(unknown)
# ['spam']
```
