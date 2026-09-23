#!/usr/bin/env python3
"""
terminal-weather — Live weather forecasts formatted for terminals.
"""
import sys
import urllib.request
import urllib.parse

def fetch_weather(city: str = "") -> str:
    loc = urllib.parse.quote(city.strip()) if city else ""
    # Use wttr.in with compact ANSI format
    url = f"https://wttr.in/{loc}?format=%l:+%c+%t+(feels+like+%f)+|+Wind:+%w+|+Humidity:+%h"
    req = urllib.request.Request(url, headers={"User-Agent": "curl/7.88.1"})
    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            return resp.read().decode("utf-8").strip()
    except Exception as e:
        return f"Weather query unavailable: {e}"

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else ""
    print("=" * 55)
    print("  Terminal Weather Forecast")
    print("=" * 55)
    print(fetch_weather(target))
    print("=" * 55)

if __name__ == "__main__":
    main()
