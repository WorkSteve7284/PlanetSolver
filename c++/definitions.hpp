#pragma once

#include <array>
#include <bit>
#include <cstdint>

using planet_index = int;
using precision = double;

constexpr precision const_cbrt(double x) {
    // Some bitwise black magic taken from
    // https://github.com/jart/cosmopolitan/blob/master/libc/tinymath/cbrt.c
    // And adjusted to work with C++ constexpr rules

    constexpr std::uint32_t
    B1 = 715094163,
    B2 = 696219795;

    constexpr double
    P0 =  1.87595182427177009643,
    P1 = -1.88497979543377169875,
    P2 =  1.621429720105354466140,
    P3 = -0.758397934778766047437,
    P4 =  0.145996192886612446982;

    double uf = x;
    std::uint64_t ui = std::bit_cast<std::uint64_t>(uf);

	double_t r,s,t,w;
	uint32_t hx = ui>>32 & 0x7fffffff;

	if (hx >= 0x7ff00000)  /* cbrt(NaN,INF) is itself */
		return x+x;

	if (hx < 0x00100000) { /* zero or subnormal? */
		uf = x*0x1p54;
        ui = std::bit_cast<std::uint64_t>(uf);
		hx = ui>>32 & 0x7fffffff;
		if (hx == 0)
			return x;  /* cbrt(0) is itself */
		hx = hx/3 + B2;
	} else
		hx = hx/3 + B1;

    ui &= 1ULL<<63;
	ui |= (uint64_t)hx << 32;

	t = std::bit_cast<double>(ui);

	r = (t*t)*(t/x);
	t = t*((P0+r*(P1+r*P2))+((r*r)*r)*(P3+r*P4));

	ui = (std::bit_cast<std::uint64_t>(t) + 0x80000000) & 0xffffffffc0000000ULL;
	t = std::bit_cast<double_t>(ui);

	s = t*t;
	r = x/s;
	w = t+t;
	r = (r-t)/(w+r);
	t = t+t*r;
	return t;
}

constexpr precision MAX_FOOD = 2000;
constexpr precision MAX_OXYGEN = 2000;
constexpr precision MAX_FUEL = 3000;

constexpr precision K_L = 0.3;
constexpr precision K_F = 0.15;

constexpr std::array<precision, 3> optimal_speeds = {
    const_cbrt((2*K_L + 1) / (2 * K_F)), // All count
    const_cbrt( (K_L + 1) / (2 * K_F)), // one count
    const_cbrt( (1) / (2 * K_F)) // None count
};