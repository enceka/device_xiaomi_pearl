#
# Copyright (C) 2025 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Inherit from pearl device
$(call inherit-product, device/xiaomi/pearl/device.mk)

PRODUCT_DEVICE := pearl
PRODUCT_NAME := lineage_pearl
PRODUCT_BRAND := Redmi
PRODUCT_MODEL := 23054RA19C
PRODUCT_MANUFACTURER := Xiaomi

PRODUCT_GMS_CLIENTID_BASE := android-xiaomi

PRODUCT_BUILD_PROP_OVERRIDES += \
    PRIVATE_BUILD_DESC="pearl-user 15 AP3A.240905.015.A2 OS2.0.205.0.VLHCNXM release-keys"

BUILD_FINGERPRINT := Xiaomi/pearl/pearl:15/AP3A.240905.015.A2/OS2.0.205.0.VLHCNXM:user/release-keys
