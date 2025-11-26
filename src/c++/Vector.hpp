#pragma once

#include <cmath>

/* Implement a Vector type (2d) */

struct Vector2 {
    double x, y;

    Vector2() : x(0), y(0) {}
    Vector2(double new_x, double new_y) : x(new_x), y(new_y) {}

    // Operators
    Vector2 operator+(const Vector2& other) const noexcept {
        return Vector2(x + other.x, y + other.y);
    }

    Vector2 operator-(const Vector2& other) const noexcept {
        return Vector2(x - other.x, y - other.y);
    }

    Vector2 operator*(double scalar) const noexcept {
        return Vector2(x * scalar, y * scalar);
    }

    Vector2 operator/(double scalar) const {
        return Vector2(x / scalar, y / scalar);
    }

    Vector2 operator-() const{ // eg -vector
        return Vector2(-x, -y);
    }

    Vector2& operator+=(const Vector2& other) noexcept {
        *this = *this + other;
        return *this;
    }

    Vector2& operator-=(const Vector2& other) noexcept {
        *this = *this - other;
        return *this;
    }

    Vector2& operator*=(double scalar) noexcept {
        *this = *this * scalar;
        return *this;
    }

    Vector2& operator/=(double scalar) {
        *this = *this / scalar;
        return *this;
    }

    bool operator==(const Vector2& other) const noexcept {
        return (x == other.x) && (y == other.y);
    }
    bool operator!=(const Vector2& other) const noexcept {
        return (x != other.x) || (y != other.y);
    }

    double sqr_magnitude() const noexcept {
        return x * x + y * y;
    }

    double magnitude() const noexcept {
        return std::sqrt(sqr_magnitude());
    }

    Vector2 normalized() const {
        return *this / magnitude();
    }

    Vector2& normalize() {
        *this = *this / magnitude();
        return *this;
    }

};

inline Vector2 operator*(double scalar, const Vector2& vec) noexcept {
    return vec * scalar;
}