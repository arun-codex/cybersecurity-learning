# Day 20 — sudo + Redirection + Command Chaining
**Planned date:** 2026-09-12

## sudo
```bash
whoami
sudo whoami
```

## Redirection
- `>` overwrite
- `>>` append

```bash
echo "SOC practice" > output.txt
echo "Second line" >> output.txt
cat output.txt
```

## Pipes
```bash
ps aux | grep firefox
ls -la | less
```

## Chaining
`&&` runs the next command when the previous command succeeds.
`;` runs the next command regardless of the previous command's result.