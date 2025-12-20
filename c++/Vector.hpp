#pragma once

#include "definitions.hpp"

struct Vector2 {
    precision x, y;

    // Constructors
    Vector2();
    Vector2(precision, precision);

    // Member functions
    precision sqr_magnitude() const noexcept;
    precision magnitude() const noexcept;
    Vector2 project(const Vector2&) const noexcept;


    // Operators
    Vector2 operator +(const Vector2&) const noexcept;
    Vector2 operator -(const Vector2&) const noexcept;
    Vector2 operator *(precision) const noexcept;

    Vector2 operator /(precision) const;

    Vector2& operator +=(const Vector2&) noexcept;
    Vector2& operator -=(const Vector2&) noexcept;
    Vector2& operator *=(precision) noexcept;
    Vector2& operator /=(precision);

    bool operator ==(const Vector2&) const noexcept;
    bool operator !=(const Vector2&) const noexcept;

    // Static functions
    static precision dot(const Vector2&, const Vector2&) noexcept;
};

inline Vector2 operator*(precision, const Vector2&) noexcept;
