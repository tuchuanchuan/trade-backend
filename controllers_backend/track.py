# coding: UTF-8

from sqlalchemy import or_

import settings
from controllers_backend.backend_base_controller import BaseController

from models.tag import Tag
from models.track import Track


class TrackListController(BaseController):
    urls = '/track/list/?'

    def get(self):
        search_type = self.get_argument('search_type')
        search_key = self.get_argument('search_key')
        track_list = []
        self.render('track/list.html', track_list=track_list)


class TrackEditController(BaseController):
    urls = '/track/edit/([0-9]+)/?'

    def get(self, track_id):
        pass

    def post(self, track_id):
        pass


class TagListController(BaseController):
    urls = '/track/tag/?'

    def get(self):
        top_tags = Tag.get_top_tags(self.orm_session)
        self.render('track/tag.html', top_tags=top_tags)


class SubTagController(BaseController):
    urls = '/track/tag/tag/?'

    def get(self):
        father_id = self.get_argument('father_id')
        tags = Tag.get_tags(father_id, self.orm_session)
        self.write(dict(
            ret=0,
            tags=[dict(name=tag.name, id=tag.id, active=tag.active, father_id=tag.father_id) for tag in tags],
        ))

    def post(self):
        tag_id = int(self.get_argument('id'))
        if not tag_id:
            tag = Tag()
            tag.father_id = self.get_argument('father_id')
        else:
            tag = self.orm_session.query(Tag).filter_by(id=tag_id).first()
        if tag:
            tag.active = self.get_argument('active')
            tag.name = self.get_argument('name')
            self.orm_session.add(tag)
            self.orm_session.commit()
        self.write(dict(ret=0))


class TrackStatusController(BaseController):
    urls = '/track/status/?'

    def get(self):
        pass
