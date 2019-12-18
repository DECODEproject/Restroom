<p align="center">
  <a href="https://www.dyne.org">
    <img alt="{project_name}" src="https://via.placeholder.com/150.png?text=LOGO" width="150" />
  </a>
</p>

<h1 align="center">
  {project_name}</br>
  <sub>{tagline}</sub>
</h1>
  
<p align="center">
  <a href="https://travis-ci.com/DECODEproject/{project_name}">
    <img src="https://travis-ci.com/DECODEproject/{project_name}.svg?branch=master" alt="Build Status">
  </a>
  <a href="https://dyne.org">
    <img src="https://img.shields.io/badge/%3C%2F%3E%20with%20%E2%9D%A4%20by-Dyne.org-blue.svg" alt="Dyne.org">
  </a>
</p>

<br><br>

<h4 align="center">
  <a href="#whale-docker">:whale: Docker</a>
  <span> • </span>
  <a href="#wrench-configuration">:wrench: Configuration</a>
  <span> • </span>
  <a href="#heart_eyes-acknowledgements">:heart_eyes: Acknowledgements</a>
  <span> • </span>
  <a href="#globe_with_meridians-links">:globe_with_meridians: Links</a>
  <span> • </span>
  <a href="#busts_in_silhouette-contributing">:busts_in_silhouette: Contributing</a>
  <span> • </span>
  <a href="#briefcase-license">:briefcase: License</a>
</h4>



<details>
 <summary><strong>:triangular_flag_on_post: Table of Contents</strong> (click to expand)</summary>

* [Docker](#whale-docker)
* [Configuration](#wrench-configuration)
* [Acknowledgements](#heart_eyes-acknowledgements)
* [Links](#globe_with_meridians-links)
* [Contributing](#busts_in_silhouette-contributing)
* [License](#briefcase-license)
</details>

***
## :whale: Docker quickstart

```bash
docker build -t restroom .
docker run -p 8000:8000 --rm -it restroom
```

head your browser to [http://localhost:8000/docs](http://localhost:8000/docs)

***
## :wrench: Configuration

Configuration available at tihs time is:

**RESTROOM_CONFIG_FILE**

That is read by `.env` or Environment variables

***
## :heart_eyes: Acknowledgements

Copyright :copyright: 2019 by [Dyne.org](https://www.dyne.org) foundation, Amsterdam

Designed, written and maintained by Puria Nafisi Azizi.

Special thanks to Jaromil for this superb idea.

<img src="https://zenroom.dyne.org/img/ec_logo.png" width="150" alt="Project funded by the European Commission">

This project is receiving funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement nr. 732546 (DECODE).


***
## :globe_with_meridians: Links

https://www.decodeproject.eu/

https://www.zenroom.org/

https://dyne.org/


***
## :busts_in_silhouette: Contributing

Please first take a look at the [Dyne.org - Contributor License Agreement](CONTRIBUTING.md) then

1.  :twisted_rightwards_arrows: [FORK IT](../../fork)
2.  Create your feature branch `git checkout -b feature/branch`
3.  Commit your changes `git commit -am 'Add some fooBar'`
4.  Push to the branch `git push origin feature/branch`
5.  Create a new Pull Request
6.  :pray: Thank you


***
## :briefcase: License
    Restroom - {tagline}
    Copyright (c) 2019 Dyne.org foundation, Amsterdam

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
