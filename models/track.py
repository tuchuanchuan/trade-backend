# coding: utf-8

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from .base import ORMBase


class Track(ORMBase):
    __tablename__ = 'track'

    id = Column(Integer, primary_key=True, nullable=False, )

    name = Column(String(128), nullable=False, )
    version = Column(String(32), nullable=False, default='', )
    composer = Column(String(512), nullable=False, default='', )
    lyricist = Column(String(512), nullable=False, default='', )
    isrc = Column(String(16), nullable=False, default='', )
    album_name = Column(String(64), nullable=False, default='', )

    file_path = Column(String, nullable=False, )
    duration = Column(Integer, nullable=False, default=0, )  # 时长，秒
    listen_url = Column(String(256), nullable=False, default='', )  # 试听链接
    wave_pic_url = Column(String(256), nullable=False, default='', )  # 波形图链接

    price = Column(Integer, nullable=False, default='', )  # 单价，分
    active = Column(Integer, nullable=False, default=0, )  # 标志上下架, 1:上架中

    # 用于记录歌曲来源，与业务无关
    copyright_id = Column(Integer, index=True, )
    is_oversea = Column(Integer, nullable=False, default=0, )

    tag_list = relationship(
        "Tag",
        secondary="track_tag_relationship",
        primaryjoin="Track.id == TrackTagRelationship.track_id",
        secondaryjoin="TrackTagRelationship.tag_id == Tag.id",
        viewonly=True,
        backref="track_list",
    )


class TrackTagRelationship(ORMBase):
    __tablename__ = 'track_tag_relationship'

    id = Column(Integer, primary_key=True, nullable=False, )
    track_id = Column(Integer, ForeignKey('track.id'))
    tag_id = Column(Integer, ForeignKey('tag.id'))

    track = relationship('Track')
    tag = relationship('Tag')
