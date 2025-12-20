#include "Vector.hpp"
#include "definitions.hpp"
#include <cmath>

// Define the Vector functions

Vector2::Vector2() : x(0), y(0) {}
Vector2::Vector2(precision X, precision Y): x(X), y(Y) {}

// Member functions
precision Vector2::sqr_magnitude() const noexcept {
    return x*x + y*y;
}

precision Vector2::magnitude() const noexcept {
    return std::sqrt(sqr_magnitude());
}

Vector2 Vector2::project(const Vector2& other) const noexcept {
    return other * (dot(*this, other) / other.sqr_magnitude());
}


// Operators
Vector2 Vector2::operator +(const Vector2& other) const noexcept {
    return Vector2{x + other.x, y + other.y};
}

Vector2 Vector2::operator -(const Vector2& other) const noexcept {
    return Vector2{x - other.x, y - other.y};
}

Vector2 Vector2::operator *(precision scalar) const noexcept {
    return Vector2{x * scalar, y * scalar};
}

Vector2 Vector2::operator /(precision scalar) const {
    return Vector2{x / scalar, y / scalar};
}

Vector2& Vector2::operator +=(const Vector2& other) noexcept {
    *this = *this + other;
    return *this;
}

Vector2& Vector2::operator -=(const Vector2& other) noexcept {
    *this = *this - other;
    return *this;
}

Vector2& Vector2::operator *=(precision scalar) noexcept {
    *this = *this * scalar;
    return *this;
}

Vector2& Vector2::operator /=(precision scalar) {
    *this = *this / scalar;
    return *this;
}

bool Vector2::operator ==(const Vector2& other) const noexcept {
    return (x == other.x) && (y == other.y);
}
bool Vector2::operator !=(const Vector2& other) const noexcept {
    return (x != other.x) || (y != other.y);
}

// Static functions
precision Vector2::dot(const Vector2& a, const Vector2& b) noexcept {
    return a.x*b.x + a.y*b.y;
}